// Command snapshotd is the backup-job daemon inherited from Norexia's founding team.
//
// It accepts snapshot jobs over HTTP, runs them on a small worker pool, and reports status.
// Storage is in memory; the real snapshot work is simulated.
package main

import (
	"log"
	"net/http"
	"os"
	"strconv"
	"time"
)

func main() {
	addr := ":8081"
	if v := os.Getenv("SNAPSHOTD_ADDR"); v != "" {
		addr = v
	}
	workers := 4
	if v := os.Getenv("SNAPSHOTD_WORKERS"); v != "" {
		n, err := strconv.Atoi(v)
		if err == nil {
			workers = n
		}
	}

	store := NewStore()
	runner := NewRunner(store, workers)
	go runner.Run()

	mux := http.NewServeMux()
	h := &Handler{store: store, runner: runner}
	mux.HandleFunc("/jobs", h.Jobs)
	mux.HandleFunc("/jobs/", h.Job)
	mux.HandleFunc("/stats", h.Stats)
	mux.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request) { w.Write([]byte("ok")) })

	srv := &http.Server{Addr: addr, Handler: mux, ReadHeaderTimeout: 5 * time.Second}
	log.Printf("snapshotd listening on %s with %d workers", addr, workers)
	log.Fatal(srv.ListenAndServe())
}
