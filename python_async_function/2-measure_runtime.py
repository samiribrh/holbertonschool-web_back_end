#!/usr/bin/env python3
"""Module to measure the runtime of a function."""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Function to measure the runtime of a function."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    totat_time = end - start
    return totat_time / n
