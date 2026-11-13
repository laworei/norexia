FROM golang:1.25-alpine AS build
WORKDIR /src
COPY go.mod ./
COPY legacy/snapshotd ./legacy/snapshotd
RUN CGO_ENABLED=0 go build -o /out/snapshotd ./legacy/snapshotd

FROM alpine:3.21
RUN adduser -D -u 10001 app
USER app
COPY --from=build /out/snapshotd /usr/local/bin/snapshotd
EXPOSE 8081
ENTRYPOINT ["/usr/local/bin/snapshotd"]
