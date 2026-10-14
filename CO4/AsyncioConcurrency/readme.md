# Asyncio & Concurrency
asyncio event loop, coroutines, async/await, Semaphore, gather, producer-consumer.
## Speedup
Sequential: O(N × t_io)  |  Asyncio: O(N/C × t_io) where C = concurrency limit
