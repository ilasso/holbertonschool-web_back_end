import asyncio

import aiohttp  # fades

all_urls = [
    "http://python.org.ar/static/img/python-footer.png",
    "http://python.org.ar/static/img/pyar-footer.png",
    "http://python.org.ar/static/img/icons/icons.png",
]


async def get_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()
    return len(content)


async def main():
    coros = []
    for url in all_urls:
        coro = get_page(url)
        coros.append(coro)
    results = await asyncio.gather(*coros)
    print("Results", results)


asyncio.run(main())
