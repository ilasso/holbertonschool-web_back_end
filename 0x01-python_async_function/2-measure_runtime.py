#!/usr/bin/env python3
"""
2-measure_runtime: module contain measure_time function
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(max_delay: int, n: int) -> float:
    """
    measure_time: function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n. Your function should return a float.
    Use the time module to measure an approximate elapsed time.
    """
    inic = time.time()
    asyncio.run(wait_n(max_delay,n))
    timed = time.time() - inic
    return timed / n
