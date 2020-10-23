#!/usr/bin/env python3

import asyncio

wait_random = __import__('0C-basic_async_syntax').wait_random

def mainrun():
    print("-----")
    print("in mainrun")
    print("-----")
    asyncio.run(wait_random(15))
    asyncio.run(wait_random(12))

asyncio.run(wait_random(15))
asyncio.run(wait_random(5))
mainrun()



#result = await asyncio.gather(wait_random(8), wait_random(12))

"""

print(asyncio.run(wait_random()))

print(asyncio.run(wait_random(5)))

print(asyncio.run(wait_random(15)))
"""
