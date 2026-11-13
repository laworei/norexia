#!/usr/bin/env python3
"""PreToolUse guard: Claude may never write to learner-owned paths.

Reads the hook JSON on stdin. Exit 2 (with a reason on stderr) denies the call.
Exit 0 with no output means "no objection".

Layers:
  * File tools (Write, Edit, MultiEdit, NotebookEdit): resolve the target and deny if it is owned.
  * Bash: deny when the command both references an owned path (or runs from one) and looks like a
    write, plus a short list of tree-mutating commands that are always denied. When unsure, deny
    and ask the learner to run the command themselves.

This is a guardrail against accidental "helping", not a sandbox. Determined circumvention
(for example an obfuscated command) is out of scope by design (brief section 13).
"""
import json
import os
import re
import shlex
import sys

FILE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}


def project_root() -> str:
    env = os.environ.get("CLAUDE_PROJECT_DIR")
    if env:
        return os.path.realpath(env)
    # .claude/hooks/guard_owned_paths.py -> repo root is two levels up
    return os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def load_owned(root: str):
    owned = []
    path = os.path.join(root, ".claude", "owned-paths.txt")
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    owned.append(line)
    except OSError:
        # Fail closed: if the list is unreadable, protect the defaults.
        owned = ["services/", "cmd/", "internal/", "pkg/", "docs/rfcs/", "docs/postmortems/", "learner/brag-doc.md"]
    return owned


def is_owned_abs(abs_path: str, root: str, owned) -> str | None:
    """Return the matching owned entry if abs_path is inside an owned path."""
    real = os.path.realpath(abs_path)
    for entry in owned:
        target = os.path.realpath(os.path.join(root, entry.rstrip("/")))
        if real == target or real.startswith(target + os.sep):
            return entry
    return None


def deny(msg: str):
    print(f"BLOCKED by ultralearning guardrail: {msg}\n"
          "Owned paths are the learner's work; Claude must not write there. "
          "Give a hint (handbook/ladder via /stuck) or ask the learner to run the command themselves.",
          file=sys.stderr)
    sys.exit(2)


# ---- Bash analysis -----------------------------------------------------------------------------

# Commands that mutate files; matched as whole words at command position or after a separator.
WRITE_WORDS = [
    r"tee", r"cp", r"mv", r"rm", r"rmdir", r"mkdir", r"touch", r"ln", r"install", r"dd", r"truncate",
    r"patch", r"chmod", r"chown", r"rsync", r"unzip", r"tar", r"curl", r"wget",
]
# Patterns that write regardless of words.
WRITE_REGEXES = [
    r"(^|[^<>&0-9])>>?(?!&)",          # output redirection (not 2>&1, not <>)
    r"\bsed\b[^|;&]*\s-[a-zA-Z]*i",    # sed -i / -Ei / -i.bak
    r"\bperl\b[^|;&]*\s-[a-zA-Z]*i",   # perl -i / -pi
    r"\b(gofmt|goimports|gofumpt)\b[^|;&]*\s-w\b",
    r"\bgolangci-lint\b[^|;&]*--fix",
    r"\bgo\s+(generate|fmt)\b",
    r"\bgo\s+mod\s+(tidy|vendor|init)\b",
    r"\bsqlc\s+generate\b",
    r"\b(buf|protoc|mockgen|stringer|wire|oapi-codegen|ent|gqlgen)\b",
    r"\bgit\s+(apply|am|restore|reset\s+--hard|clean|stash|cherry-pick|merge|rebase|pull|revert|mv|rm)\b",
    r"\bgit\s+checkout\s+(\S+\s+)?--(\s|$)",
    r"\b(python3?|node|ruby|perl|php|deno|bun|osascript)\b[^|;&]*\s-(c|e|p)\b",  # inline interpreters
    r"\b(python3?|node|ruby|perl|php|deno|bun)\s+<<",                           # heredoc interpreters
    r"\b(open|write_text|writeFileSync|File\.write)\b",
]
ALWAYS_DENY = [
    (r"\bgit\s+(apply|am)\b", "git apply/am can rewrite owned files"),
    (r"\bpatch\b", "patch can rewrite owned files"),
]


def owned_mentions(command: str, owned) -> list[str]:
    """Owned entries that the command text seems to reference."""
    hits = []
    for entry in owned:
        e = entry.rstrip("/")
        # Match path as a token start or after a quote/=/space/./ prefix, e.g. services/x, ./services, "services".
        # Not preceded by an arbitrary "/" so URLs/module paths like golang.org/x/vuln/cmd/foo are not mistaken for
        # the repo's cmd/. Absolute paths into the repo are matched separately via absolute_hits.
        pat = r"(?:^|[\s'\"=:(,]|\./|\.\./)" + re.escape(e) + r"(?:/|$|['\"\s;|&)])"
        if re.search(pat, command):
            hits.append(entry)
    return hits


def looks_like_write(command: str) -> bool:
    for rx in WRITE_REGEXES:
        if re.search(rx, command):
            return True
    words = "|".join(WRITE_WORDS)
    if re.search(rf"(?:^|[;&|`(]\s*|\s)(?:sudo\s+)?(?:{words})(?:\s|$)", command):
        return True
    return False


def check_bash(command: str, cwd: str, root: str, owned):
    for rx, why in ALWAYS_DENY:
        if re.search(rx, command):
            deny(f"{why}. Ask the learner to run it.")

    # Is the shell running from inside an owned path?
    cwd_owned = is_owned_abs(cwd, root, owned) if cwd else None
    # Does it `cd` into one?
    cd_owned = None
    for m in re.finditer(r"\bcd\s+([^\s;&|]+)", command):
        target = m.group(1).strip("'\"")
        absd = target if os.path.isabs(target) else os.path.join(cwd or root, target)
        cd_owned = cd_owned or is_owned_abs(absd, root, owned)

    mentions = owned_mentions(command, owned)
    absolute_hits = [e for e in owned if os.path.join(root, e.rstrip("/")) in command]
    mentions = list(dict.fromkeys(mentions + absolute_hits))

    if (mentions or cwd_owned or cd_owned) and looks_like_write(command):
        where = ", ".join(mentions) or (cwd_owned or cd_owned)
        deny(f"command looks like a write and touches owned path(s): {where}.")

    # git checkout/switch of a path-less tree is fine, but `git checkout .`/`restore .` can clobber owned files.
    if re.search(r"\bgit\s+(checkout|restore)\s+(--\s+)?\.(\s|$)", command):
        deny("git checkout/restore of '.' can overwrite owned files.")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        print("guard_owned_paths: could not parse hook input; failing closed.", file=sys.stderr)
        sys.exit(2)

    tool = data.get("tool_name", "")
    tin = data.get("tool_input") or {}
    cwd = data.get("cwd") or os.getcwd()
    root = project_root()
    owned = load_owned(root)

    if tool in FILE_TOOLS:
        raw = tin.get("file_path") or tin.get("notebook_path") or ""
        if not raw:
            sys.exit(0)
        abs_path = raw if os.path.isabs(raw) else os.path.join(cwd, raw)
        hit = is_owned_abs(abs_path, root, owned)
        if hit:
            deny(f"{tool} target '{raw}' is inside owned path '{hit}'.")
        sys.exit(0)

    if tool == "Bash":
        check_bash(tin.get("command", ""), cwd, root, owned)
        sys.exit(0)

    sys.exit(0)


if __name__ == "__main__":
    main()
