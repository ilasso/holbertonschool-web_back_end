# Python >= 3.7

import asyncio
import datetime


async def display_date():
    remaining = 5
    while True:
        print(datetime.datetime.now())
        remaining -= 1
        if not remaining:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())
