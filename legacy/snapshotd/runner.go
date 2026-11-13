package main

import (
	"log"
	"math/rand"
	"time"
)

// Runner executes queued jobs on a fixed pool of workers.
type Runner struct {
	store   *Store
	workers int
	queue   chan int

	// per-project bookkeeping used by /stats
	lastRun map[string]time.Time
	runs    int
}

func NewRunner(store *Store, workers int) *Runner {
	return &Runner{
		store:   store,
		workers: workers,
		queue:   make(chan int, 64),
		lastRun: map[string]time.Time{},
	}
}

// Enqueue schedules a job. If the queue is full the job is dropped.
func (r *Runner) Enqueue(id int) {
	select {
	case r.queue <- id:
	default:
		log.Printf("queue full, dropping job %d", id)
	}
}

// Run starts the workers. It never returns.
func (r *Runner) Run() {
	for i := 0; i < r.workers; i++ {
		go r.worker(i)
	}
	select {}
}

func (r *Runner) worker(n int) {
	for id := range r.queue {
		job, err := r.store.Get(id)
		if err != nil {
			continue
		}
		job.Status = "running"
		job.Attempts++
		start := time.Now()

		// simulated snapshot
		time.Sleep(time.Duration(20+rand.Intn(60)) * time.Millisecond)
		if rand.Intn(10) == 0 {
			job.Status = "failed"
			log.Printf("worker %d: job %d failed", n, id)
			r.lastRun[job.Project] = time.Now()
			r.runs++
			continue
		}

		job.Result = &Result{Bytes: int64(rand.Intn(1 << 20)), Duration: time.Since(start)}
		job.Status = "done"
		r.lastRun[job.Project] = time.Now()
		r.runs++
	}
}
