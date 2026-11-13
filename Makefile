.PHONY: check fmt vet lint test cover vuln state hooks docs ci

GO ?= go

# Local gate: same things CI runs for Go (fmt, vet, lint, unit tests with -race).
check: fmt vet lint test

fmt:
	@out=$$(gofmt -l $$(git ls-files '*.go' 2>/dev/null; git ls-files --others --exclude-standard '*.go' 2>/dev/null)); \
	if [ -n "$$out" ]; then echo "gofmt needed on:"; echo "$$out"; exit 1; fi

vet:
	$(GO) vet ./...

lint:
	golangci-lint run ./...

test:
	$(GO) test -race -cover ./...

cover:
	python3 scripts/coverage-floor.py

vuln:
	govulncheck ./...

# Program machinery (not learner code)
state:
	python3 scripts/validate-state

hooks:
	./scripts/test-hooks.sh

docs:
	python3 scripts/gen-competencies.py

ci: check vuln state hooks
