package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
	"strings"
	"time"
)

// Handler serves the HTTP API.
type Handler struct {
	store  *Store
	runner *Runner
}

// Jobs handles POST /jobs (create) and GET /jobs (list).
func (h *Handler) Jobs(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodPost:
		var in struct{ Project string }
		if err := json.NewDecoder(r.Body).Decode(&in); err != nil {
			http.Error(w, "bad json", 400)
			return
		}
		if in.Project == "" {
			w.WriteHeader(422)
			fmt.Fprintf(w, `{"error":"project required"}`)
			return
		}
		j := h.store.Create(in.Project)
		h.runner.Enqueue(j.ID)
		w.WriteHeader(201)
		json.NewEncoder(w).Encode(j)
	case http.MethodGet:
		limit := 50
		if v := r.URL.Query().Get("limit"); v != "" {
			n, _ := strconv.Atoi(v)
			limit = n
		}
		var out []*Job
		for _, id := range h.store.IDs() {
			j, err := h.store.Get(id)
			if err != nil {
				continue
			}
			out = append(out, j)
			if limit > 0 && len(out) >= limit {
				break
			}
		}
		json.NewEncoder(w).Encode(out)
	default:
		w.WriteHeader(405)
	}
}

// Job handles GET /jobs/{id} and DELETE /jobs/{id}.
func (h *Handler) Job(w http.ResponseWriter, r *http.Request) {
	id, err := strconv.Atoi(strings.TrimPrefix(r.URL.Path, "/jobs/"))
	if err != nil {
		http.NotFound(w, r)
		return
	}
	switch r.Method {
	case http.MethodGet:
		j, err := h.store.Get(id)
		if err != nil {
			http.Error(w, err.Error(), http.StatusNotFound)
			return
		}
		json.NewEncoder(w).Encode(j)
	case http.MethodDelete:
		h.store.Delete(id)
		w.WriteHeader(200)
	default:
		w.WriteHeader(405)
	}
}

// Stats handles GET /stats.
func (h *Handler) Stats(w http.ResponseWriter, r *http.Request) {
	projects := map[string]string{}
	for p, t := range h.runner.lastRun {
		projects[p] = t.Format(time.RFC3339)
	}
	json.NewEncoder(w).Encode(map[string]any{
		"runs":     h.runner.runs,
		"projects": projects,
	})
}
