#!/usr/bin/env python3
"basics of async"
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    "measure the time of running the wait_t function"
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    t = time.perf_counter() - s
    return t / n
