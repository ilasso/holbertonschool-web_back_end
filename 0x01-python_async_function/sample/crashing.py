import asyncio


async def calc(number):
    """Very expensive calculation."""
    return 3.14 / number


async def main():
    numbers = [4, 2, 0, 7]

    print("--------- sequential")
    for n in numbers:
        try:
            resp = await calc(n)
        except Exception as err:
            print("Crash", n, err)
        else:
            print("Result", n, resp)

    print("--------- parallel")
    coros = [calc(n) for n in numbers]
    results = await asyncio.gather(*coros, return_exceptions=True)
    for n, result in zip(numbers, results):
        if isinstance(result, Exception):
            print("Crash", n, result)
        else:
            print("Result", n, result)


asyncio.run(main())
