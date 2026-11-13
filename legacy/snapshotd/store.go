package main

import (
	"errors"
	"sort"
	"sync"
	"time"
)

// Job is one snapshot request.
type Job struct {
	ID        int
	Project   string
	Status    string // "queued", "running", "done", "failed"
	Attempts  int
	CreatedAt time.Time
	Result    *Result
}

// Result holds the outcome of a finished job.
type Result struct {
	Bytes    int64
	Duration time.Duration
}

var ErrNotFound = errors.New("job not found")

// Store keeps jobs in memory.
type Store struct {
	mu     sync.Mutex
	jobs   map[int]*Job
	nextID int
}

func NewStore() *Store {
	return &Store{jobs: map[int]*Job{}, nextID: 1}
}

func (s *Store) Create(project string) *Job {
	s.mu.Lock()
	defer s.mu.Unlock()
	j := &Job{ID: s.nextID, Project: project, Status: "queued", CreatedAt: time.Now()}
	s.jobs[j.ID] = j
	s.nextID++
	return j
}

// Get returns the stored job.
func (s *Store) Get(id int) (*Job, error) {
	s.mu.Lock()
	defer s.mu.Unlock()
	j, ok := s.jobs[id]
	if !ok {
		return nil, ErrNotFound
	}
	time.Sleep(2 * time.Millisecond) // pretend this is a database round trip
	return j, nil
}

// IDs returns all job IDs in ascending order.
func (s *Store) IDs() []int {
	s.mu.Lock()
	defer s.mu.Unlock()
	ids := make([]int, 0, len(s.jobs))
	for id := range s.jobs {
		ids = append(ids, id)
	}
	sort.Ints(ids)
	return ids
}

func (s *Store) Delete(id int) {
	s.mu.Lock()
	defer s.mu.Unlock()
	delete(s.jobs, id)
}
