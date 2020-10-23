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

loop = asyncio.get_event_loop()
loop.run_until_complete(display_date())
loop.close()
