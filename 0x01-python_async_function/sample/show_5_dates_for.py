import asyncio
import datetime


class DateGenerator:
    def __init__(self, limit):
        self.limit = limit

    def __aiter__(self):
        return self

    async def __anext__(self):
        if not self.limit:
            raise StopAsyncIteration

        self.limit -= 1
        await asyncio.sleep(1)
        return datetime.datetime.now()


async def display_date():
    async for date in DateGenerator(5):
        print(date)

loop = asyncio.get_event_loop()
loop.run_until_complete(display_date())
