#!/usr/bin/env python3
"""
If you run this code, you will get a TypeError:
‘async for’ requires an object with __aiter__ method,
got range. What you really want to do is call another
async def function instead of calling range directly.
Here’s an example:
"""
import asyncio

async def numbers(numbers):
    for i in range(numbers):
        yield i
        await asyncio.sleep(0.5)

async def main():
    odd_numbers = [i async for i in numbers(10) if i % 2]
    print(odd_numbers)

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()
