#!/usr/bin/env python3
"""
1-concurrent_coroutines: module contain wait_n function
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int) -> List[float]:
    """
    wait_n:
    Import wait_random from the previous python file that you’ve written
    and write an async routine called wait_n that takes in 2 int arguments:
    max_delay and n. You will spawn wait_random n times with the specified
    max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without
    using sort() because of concurrency.
    """
    # way 1
    """
    waitrandom = [wait_random(n)
                  for i in range(max_delay)]
    return sorted([await i for i in waitrandom])
    """
    # way 2 more quick because as_completed notify when
    # each task is finishing
    lista: List[float] = []
    for i in range(max_delay):
        lista.append(wait_random(n))
    return [await i for i in asyncio.as_completed(lista)]
