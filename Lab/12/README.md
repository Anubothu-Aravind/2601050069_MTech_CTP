# Asynchronous I/O and Concurrency using asyncio

## Objective

Build a high-performance asynchronous data fetcher using Python's `asyncio` event loop, coroutines, `async/await`, Semaphore rate-limiting, and analyze its speedup relative to single-threaded sequential execution.

## Problem Statement

When fetching records from external web services, relational databases, or cloud endpoints, the application spends the vast majority of time blocked on network I/O. A sequential program wastes CPU cycles waiting for sockets to respond ($T_{total} = \sum t_i$). By using cooperative multitasking via the `asyncio` event loop and bounding concurrency with a semaphore, the system achieves maximum throughput without exhausting server resources or socket descriptors.

## Key Concurrency Concepts

- **Event Loop**: Schedules and executes asynchronous tasks collaboratively on a single OS thread, circumventing GIL bottlenecks for I/O-bound workflows.
- **Coroutines (`async/await`)**: Functions that can pause execution (`await`) during I/O operations and yield control back to the event loop.
- **`asyncio.Semaphore`**: Prevents denial-of-service and socket starvation by enforcing a strict concurrency upper bound (e.g., maximum 5 active requests).
- **`asyncio.gather`**: Concurrently fires multiple tasks and aggregates results upon completion.

## Python Program

The implementation is located in:

`Asyncio_Concurrent_Crawler.ipynb`

### Sample Output

```text
Processed 20 requests concurrently.
Max Concurrent Workers: 5
Total Async Duration: 0.208 seconds
Equivalent Sequential Duration would be: 1.000 seconds
Speedup Factor: 4.81x
Sample Result: {'resource_id': 1, 'status': 200, 'data': 'Payload for record #1'}
```

## Performance Benchmark

| Metric | Sequential Execution | Asyncio Concurrency (Limit = 5) |
|---|---|---|
| Total Tasks | 20 | 20 |
| Latency per Task | 50 ms | 50 ms |
| Total Elapsed Time | ~1.00 s | ~0.21 s |
| Speedup Factor | Baseline (1.0x) | **~4.8x** |
| Thread Overhead | Low (Single Thread) | Minimal (Single Thread + Event Loop) |

## Complexity Analysis

- **Time Complexity**: $O(\frac{N}{C} \cdot t_{io})$ where $N$ is total requests, $C$ is semaphore concurrency, and $t_{io}$ is average I/O latency.
- **Space Complexity**: $O(N)$ memory for task descriptors and event loop callback queues.

## How to Run

1. Open `Asyncio_Concurrent_Crawler.ipynb` in Jupyter Notebook.
2. Select Python 3 kernel.
3. Run all cells to benchmark async event loop concurrency against sequential execution.
