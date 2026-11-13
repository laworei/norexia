#!/usr/bin/env bash
# Feeds sample PreToolUse inputs to the owned-path guard and asserts allow/deny.
# Usage: scripts/test-hooks.sh        (exit 0 = all pass)
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOK="$ROOT/.claude/hooks/guard_owned_paths.py"
export CLAUDE_PROJECT_DIR="$ROOT"
pass=0; fail=0

# expect <allow|deny> <description> <tool_name> <json tool_input> [cwd]
expect() {
  local want="$1" desc="$2" tool="$3" input="$4" cwd="${5:-$ROOT}"
  local payload rc
  payload=$(jq -nc --arg t "$tool" --argjson i "$input" --arg c "$cwd" '{tool_name:$t,tool_input:$i,cwd:$c}')
  printf '%s' "$payload" | python3 "$HOOK" >/dev/null 2>&1
  rc=$?
  local got="allow"; [ "$rc" -eq 2 ] && got="deny"
  if [ "$got" = "$want" ]; then pass=$((pass+1)); printf 'ok    %-5s %s\n' "$want" "$desc"
  else fail=$((fail+1)); printf 'FAIL  want=%s got=%s (rc=%s) %s\n' "$want" "$got" "$rc" "$desc"; fi
}
bash_in() { jq -nc --arg c "$1" '{command:$c}'; }
file_in() { jq -nc --arg p "$1" '{file_path:$p,content:"x"}'; }

echo "== file tools: owned paths denied =="
for t in Write Edit MultiEdit; do
  expect deny "$t services/x.go"            "$t" "$(file_in services/api/main.go)"
  expect deny "$t abs internal/x.go"        "$t" "$(file_in "$ROOT/internal/x.go")"
  expect deny "$t cmd/main.go"              "$t" "$(file_in cmd/norexia/main.go)"
  expect deny "$t pkg/x.go"                 "$t" "$(file_in pkg/x.go)"
  expect deny "$t docs/rfcs/0001.md"        "$t" "$(file_in docs/rfcs/0001.md)"
  expect deny "$t docs/postmortems/p.md"    "$t" "$(file_in docs/postmortems/p.md)"
  expect deny "$t brag-doc"                 "$t" "$(file_in learner/brag-doc.md)"
  expect deny "$t traversal via .."         "$t" "$(file_in docs/../services/x.go)"
done
expect deny "NotebookEdit in services"     NotebookEdit "$(jq -nc '{notebook_path:"services/n.ipynb"}')"
expect deny "relative path with cwd inside owned" Write "$(file_in x.go)" "$ROOT/services"

echo "== file tools: allowed paths permitted =="
expect allow "Write company/WORLD.md"      Write "$(file_in company/WORLD.md)"
expect allow "Write handbook/x.md"         Write "$(file_in handbook/x.md)"
expect allow "Write docs/PROGRAM.md"       Write "$(file_in docs/PROGRAM.md)"
expect allow "Write docs/adr/0001.md"      Write "$(file_in docs/adr/0001.md)"
expect allow "Write learner/profile.yaml"  Write "$(file_in learner/profile.yaml)"
expect allow "Write legacy/main.go"        Write "$(file_in legacy/main.go)"
expect allow "Write .claude/skills/x"      Write "$(file_in .claude/skills/x/SKILL.md)"
expect allow "Write .sealed/key.md"        Write "$(file_in .sealed/key.md)"
expect allow "Write scripts/x.sh"          Write "$(file_in scripts/x.sh)"
expect allow "Write platform/ (pre-L3)"    Write "$(file_in platform/compose.yaml)"
expect allow "Write services-notes (prefix lookalike)" Write "$(file_in services-notes.md)"

echo "== bash: writes to owned paths denied =="
expect deny "redirect >"            Bash "$(bash_in 'echo hi > services/a.go')"
expect deny "redirect >>"           Bash "$(bash_in 'echo hi >> internal/a.go')"
expect deny "cat heredoc redirect"  Bash "$(bash_in "cat > cmd/main.go <<'EOF'
package main
EOF")"
expect deny "tee"                   Bash "$(bash_in 'echo x | tee pkg/a.go')"
expect deny "sed -i"                Bash "$(bash_in "sed -i '' 's/a/b/' services/a.go")"
expect deny "sed -i.bak"            Bash "$(bash_in "sed -i.bak 's/a/b/' services/a.go")"
expect deny "perl -pi"              Bash "$(bash_in "perl -pi -e 's/a/b/' internal/a.go")"
expect deny "cp into owned"         Bash "$(bash_in 'cp legacy/main.go services/main.go')"
expect deny "mv into owned"         Bash "$(bash_in 'mv tmp.go internal/x.go')"
expect deny "rm owned"              Bash "$(bash_in 'rm -rf services/old')"
expect deny "mkdir owned"           Bash "$(bash_in 'mkdir -p services/api')"
expect deny "touch owned"           Bash "$(bash_in 'touch docs/rfcs/0001.md')"
expect deny "git apply"             Bash "$(bash_in 'git apply fix.patch')"
expect deny "git am"                Bash "$(bash_in 'git am 0001.patch')"
expect deny "patch"                 Bash "$(bash_in 'patch -p1 < fix.diff')"
expect deny "git checkout -- owned" Bash "$(bash_in 'git checkout -- services/a.go')"
expect deny "git restore owned"     Bash "$(bash_in 'git restore services/a.go')"
expect deny "git checkout ."        Bash "$(bash_in 'git checkout .')"
expect deny "gofmt -w owned"        Bash "$(bash_in 'gofmt -w services/')"
expect deny "goimports -w owned"    Bash "$(bash_in 'goimports -w internal/')"
expect deny "go generate owned"     Bash "$(bash_in 'go generate ./internal/...')"
expect deny "sqlc generate"         Bash "$(bash_in 'cd services/api && sqlc generate')"
expect deny "cd owned then write"   Bash "$(bash_in 'cd services && echo x > a.go')"
expect deny "write from owned cwd"  Bash "$(bash_in 'echo x > a.go')" "$ROOT/internal"
expect deny "python inline write"   Bash "$(bash_in "python3 -c \"open('services/a.go','w').write('x')\"")"
expect deny "node inline write"     Bash "$(bash_in "node -e \"require('fs').writeFileSync('cmd/a.go','x')\"")"
expect deny "absolute path write"   Bash "$(bash_in "echo x > $ROOT/pkg/a.go")"
expect deny "brag doc write"        Bash "$(bash_in 'echo x >> learner/brag-doc.md')"
expect deny "postmortem write"      Bash "$(bash_in 'cp t.md docs/postmortems/p.md')"

echo "== bash: reads and allowed writes permitted =="
expect allow "ls owned"             Bash "$(bash_in 'ls services/ internal/')"
expect allow "cat owned"            Bash "$(bash_in 'cat services/api/main.go')"
expect allow "grep owned"           Bash "$(bash_in 'grep -rn TODO services/ internal/')"
expect allow "go test"              Bash "$(bash_in 'go test -race ./...')"
expect allow "go vet"               Bash "$(bash_in 'go vet ./services/...')"
expect allow "golangci-lint run"    Bash "$(bash_in 'golangci-lint run ./...')"
expect allow "git status"           Bash "$(bash_in 'git status --short')"
expect allow "git diff owned"       Bash "$(bash_in 'git diff -- services/')"
expect allow "git log"              Bash "$(bash_in 'git log --oneline -- internal/')"
expect allow "git add/commit"       Bash "$(bash_in 'git add company/ && git commit -m "x"')"
expect allow "echo to company"      Bash "$(bash_in 'echo x > company/state.yaml')"
expect allow "tee to learner state" Bash "$(bash_in 'echo {} | tee learner/findings.jsonl')"
expect allow "mkdir handbook"       Bash "$(bash_in 'mkdir -p handbook/templates')"
expect allow "cp into legacy"       Bash "$(bash_in 'cp a.go legacy/a.go')"
expect allow "gofmt -l legacy"      Bash "$(bash_in 'gofmt -l legacy/')"
expect allow "gh issue list"        Bash "$(bash_in 'gh issue list')"
expect allow "docker compose up"    Bash "$(bash_in 'docker compose -f platform/compose.yaml up -d')"
expect allow "2>&1 not a write"     Bash "$(bash_in 'go build ./services/... 2>&1 | head')"
expect allow "go build owned (read)" Bash "$(bash_in 'go build -o /dev/null ./services/...')"
expect allow "make check"           Bash "$(bash_in 'make check')"
expect allow "go install module path with /cmd/" Bash "$(bash_in 'go install golang.org/x/vuln/cmd/govulncheck@latest')"
expect deny  "parent-relative write" Bash "$(bash_in 'cp x.go ../services/x.go')" "$ROOT/docs"
expect deny  "dot-slash write"       Bash "$(bash_in 'echo x > ./internal/x.go')"

echo
echo "passed=$pass failed=$fail"
[ "$fail" -eq 0 ]
