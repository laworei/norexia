# Go style anchors and conflict resolution

Reviews cite these, not personal taste:

1. [Effective Go](https://go.dev/doc/effective_go)
2. [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments)
3. [Google Go Style Guide](https://google.github.io/styleguide/go/)
4. [Uber Go Style Guide](https://github.com/uber-go/guide/blob/master/style.md)
5. The standard library as the tie-breaker for naming and structure.

## When they disagree
- **Official Go docs and Code Review Comments win** over the two company guides.
- **Google over Uber** on naming, comments and package layout. **Uber over Google** only where it is a concrete correctness rule (for example "copy slices and maps at boundaries", "don't use fire-and-forget goroutines").
- **Error handling:** wrap with `%w` when callers may need the cause; do not wrap just to add a stack. Error strings are lower case, without punctuation.
- **Interfaces:** define at the consumer, keep small, return concrete types.
- **Concurrency:** every goroutine has an owner and a way to stop. `context.Context` is the first parameter.
- **Formatting:** `gofmt`/`goimports` are not a debate.
- **Testing:** table-driven with subtests; fakes over mocks for owned interfaces; `t.Helper()` in helpers.
- If a case is still unclear, write a one-paragraph ADR in `docs/adr/` and cite it.
