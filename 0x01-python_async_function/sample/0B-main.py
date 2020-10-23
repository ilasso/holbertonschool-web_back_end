#!/usr/bin/env python3

import asyncio

wait_random = __import__('0B-basic_async_syntax').wait_random

#print(asyncio.run(wait_random()))
#print("1")
#print(asyncio.run(wait_random(5)))
#print("2")
#print(asyncio.run(wait_random(15)))
#print("3")

async def main():
    print("Inic Main")
    result = await asyncio.gather(wait_random(), wait_random(5), wait_random(0))
    print(asyncio.current_task())
    print(asyncio.__all__)

    return result

resultado = asyncio.run(main())
print(resultado)
print(type(resultado))
print("Finished Main")
