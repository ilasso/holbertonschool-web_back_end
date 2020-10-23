#!/usr/bin/env python3
"""0-basic_async_syntax: module to include wait_random function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random: asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits
    for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.Use the random module.
    """
    print(f"Inic max_delay={max_delay}")
    flt = random.uniform(0, max_delay)
    await asyncio.sleep(flt)
    print(f"Finish max_delay={max_delay}")
    return flt
