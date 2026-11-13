---
name: review
description: Staff-engineer review of one of the learner's pull requests (and specialist reviews by path). Use when the learner types /review <PR#>.
argument-hint: <pr-number>
disable-model-invocation: true
context: fork
agent: staff-engineer
allowed-tools: Bash(gh pr *) Bash(gh issue view *) Bash(gh api -X POST repos/laworei/norexia/issues/*) Bash(gh api -X DELETE repos/laworei/norexia/issues/*) Bash(gh api *) Bash(git *) Bash(go test *) Bash(go vet *) Bash(make *) Bash(golangci-lint *)
---

Review pull request **#$ARGUMENTS** in `laworei/norexia` following your protocol exactly.

1. `gh pr view $ARGUMENTS --json title,body,files,headRefName,labels,closingIssuesReferences` and read the linked issue.
2. Check out the branch read-only for inspection (do not commit to it). Run `make check` if it exists, otherwise `gofmt -l`, `go vet ./...`, `go test -race ./...`. Exercise the changed behavior.
3. Decide which specialists are needed from the changed paths: security-engineer for auth, payments, secrets, `go.mod`, Dockerfile, Compose/Kubernetes/IaC; sre-lead for deploy, config, observability. Run their reviews in the same pass using their checklists and headers, as separate comments.
4. Post one review comment under your persona header with the findings, labelled and evidenced. Set the label `review:approved` or `review:changes-requested` and remove the other, using the REST API (`gh pr edit --add-label` needs an extra token scope): `gh api -X POST repos/laworei/norexia/issues/<PR>/labels -f 'labels[]=review:approved'` and `gh api -X DELETE repos/laworei/norexia/issues/<PR>/labels/review:changes-requested` (ignore 404 on the delete).
5. Append each finding to `learner/findings.jsonl` and update `recurrence_count` using earlier findings with the same subcode in the last 30 days.
6. Add a line to `learner/journal.md`. Report to the learner: verdict, the top 3 points, and what to reply to before merge (every `blocking` or `should-fix` comment needs a reply from the learner).

Do not post a fix. Do not edit anything under an owned path.
