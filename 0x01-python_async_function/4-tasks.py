#!/usr/bin/env python3
"""4-tasks: module contain task_wait_n function
"""
import asyncio
import bisect
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n:
    Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is being
    called.
    """
    lista: List[float] = []
    for i in range(n):
        lista.append(task_wait_random(max_delay))
    return [await i for i in asyncio.as_completed(lista)]
