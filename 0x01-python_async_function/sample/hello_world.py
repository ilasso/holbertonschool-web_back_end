import asyncio


async def hello_world():
    print("Hello World!")

loop = asyncio.get_event_loop()
coro = hello_world()
loop.run_until_complete(coro)
