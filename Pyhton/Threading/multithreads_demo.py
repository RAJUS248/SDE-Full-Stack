#!/usr/bin/env python3
"""
Multithreading Demo: Show which thread performed which task.

Features
--------
- Configurable number of threads and total tasks
- Simulated work (1 second per task by default)
- Clear console output with thread names and timestamps
- Summary table per run + wall-clock duration
- `--demo` to run sequentially with 1, 5, and 10 threads

Usage
-----
# Single run (25 tasks, 5 threads)
python multithread_demo.py --threads 5 --tasks 25

# Demo runs: 1, 5, and 10 threads
python multithread_demo.py --demo

# Customize simulated work duration (milliseconds)
python multithread_demo.py --threads 5 --tasks 25 --work-ms 1000
"""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import logging
import random
import signal
import sys
import threading
import time
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Iterable, List, Tuple


# ------------------------------- Data Models ------------------------------- #

@dataclass
class Task:
    """A unit of work for the demo."""
    task_id: int
    kind: str  # e.g., "Generate Document" or "Compute Sum"

@dataclass
class TaskResult:
    """Result and telemetry captured for each task."""
    task_id: int
    kind: str
    thread_name: str
    start_ts: float
    end_ts: float

    @property
    def duration_ms(self) -> int:
        return int((self.end_ts - self.start_ts) * 1000)

    @property
    def start_str(self) -> str:
        return datetime.fromtimestamp(self.start_ts).strftime("%H:%M:%S.%f")[:-3]

    @property
    def end_str(self) -> str:
        return datetime.fromtimestamp(self.end_ts).strftime("%H:%M:%S.%f")[:-3]


# ------------------------------ Task Generator ----------------------------- #

def build_tasks(count: int, *, seed: int = 42) -> List[Task]:
    """
    Create a deterministic list of 'count' tasks with two simple kinds.
    Deterministic so your class sees consistent assignments across runs.
    """
    rng = random.Random(seed)
    kinds = ["Generate Document", "Compute Sum"]
    tasks = [Task(task_id=i + 1, kind=rng.choice(kinds)) for i in range(count)]
    return tasks


# ------------------------------ Worker Function ---------------------------- #

def do_work(task: Task, work_ms: int) -> TaskResult:
    """
    Simulate doing 'task' by sleeping for 'work_ms'.
    Returns timing and thread info for later reporting.
    """
    thread_name = threading.current_thread().name
    start_ts = time.time()

    # Optional: pretend to do different fake work by kind (always 1s sleep).
    # This is intentionally simple so concurrency benefits are obvious.
    time.sleep(work_ms / 1000.0)

    end_ts = time.time()

    logging.info(
        "Task %-3d | %-17s | Start: %s | End: %s | Thread: %s",
        task.task_id,
        task.kind,
        datetime.fromtimestamp(start_ts).strftime("%H:%M:%S"),
        datetime.fromtimestamp(end_ts).strftime("%H:%M:%S"),
        thread_name,
    )

    return TaskResult(
        task_id=task.task_id,
        kind=task.kind,
        thread_name=thread_name,
        start_ts=start_ts,
        end_ts=end_ts,
    )


# ------------------------------- Orchestrator ------------------------------ #

def run_batch(num_threads: int, total_tasks: int, work_ms: int) -> Tuple[List[TaskResult], float]:
    """
    Run 'total_tasks' across a thread pool with 'num_threads' workers.
    Returns (results, wall_clock_seconds).
    """
    tasks = build_tasks(total_tasks)
    results: List[TaskResult] = []

    logging.info("\n=== RUN START: %d tasks on %d threads (work: %d ms) ===",
                 total_tasks, num_threads, work_ms)
    t0 = time.perf_counter()

    # ThreadPoolExecutor assigns readable names with thread_name_prefix
    with futures.ThreadPoolExecutor(max_workers=num_threads,
                                    thread_name_prefix="Worker") as executor:
        future_map = {executor.submit(do_work, task, work_ms): task.task_id for task in tasks}
        try:
            for f in futures.as_completed(future_map):
                results.append(f.result())
        except KeyboardInterrupt:
            logging.warning("KeyboardInterrupt: canceling outstanding tasks...")
            # Best-effort cancellation (running tasks can't be interrupted mid-sleep)
            for f in future_map:
                f.cancel()
            raise

    t1 = time.perf_counter()
    wall_clock = t1 - t0
    logging.info("=== RUN END: %d tasks on %d threads | Wall time: %.3f s ===\n",
                 total_tasks, num_threads, wall_clock)
    return results, wall_clock


# --------------------------------- Output ---------------------------------- #

def print_summary(results: Iterable[TaskResult], wall_seconds: float) -> None:
    """
    Print a stable, easy-to-read summary table for the batch.
    """
    results_sorted = sorted(results, key=lambda r: r.task_id)

    header = (
        "Task  Kind                Thread       Start Time     End Time       Duration(ms)"
    )
    line = "-" * len(header)
    print(header)
    print(line)
    for r in results_sorted:
        print(f"{r.task_id:<5} {r.kind:<18} {r.thread_name:<11} "
              f"{r.start_str:<14} {r.end_str:<14} {r.duration_ms:>12}")

    print(line)
    print(f"Total Tasks: {len(results_sorted)}")
    print(f"Wall-Clock Time: {wall_seconds:.3f} seconds\n")


# --------------------------------- CLI ------------------------------------- #

def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Demonstrate Python multithreading with a thread pool and clear task/thread output."
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "--demo",
        action="store_true",
        help="Run three sequential batches with 1, 5, and 10 threads (25 tasks each).",
    )
    group.add_argument(
        "--threads", type=int, default=None,
        help="Number of worker threads for a single run.",
    )
    parser.add_argument(
        "--tasks", type=int, default=25,
        help="Total number of tasks to process (default: 25).",
    )
    parser.add_argument(
        "--work-ms", type=int, default=1000,
        help="Simulated work duration per task in milliseconds (default: 1000).",
    )
    parser.add_argument(
        "--log-level", default="INFO",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"],
        help="Logging verbosity (default: INFO).",
    )
    return parser.parse_args(argv)


def setup_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(message)s",  # clean, single-line log output
    )


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    setup_logging(args.log_level)

    # Graceful Ctrl+C on Windows/Linux/Mac
    signal.signal(signal.SIGINT, lambda *_: (_ for _ in ()).throw(KeyboardInterrupt))

    try:
        if args.demo:
            # Demo: sequentially run 1, 5, and 10 threads
            for n_threads in (1, 5, 10):
                results, wall = run_batch(num_threads=n_threads, total_tasks=args.tasks, work_ms=args.work_ms)
                print_summary(results, wall_seconds=wall)
        else:
            n_threads = args.threads if args.threads is not None else 5
            results, wall = run_batch(num_threads=n_threads, total_tasks=args.tasks, work_ms=args.work_ms)
            print_summary(results, wall_seconds=wall)

    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
        return 130  # 128 + SIGINT

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
