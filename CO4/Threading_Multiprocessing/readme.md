# Threading vs Multiprocessing
GIL prevents CPU-bound thread parallelism. Use `multiprocessing` for CPU tasks, `asyncio`/`threading` for I/O tasks.
