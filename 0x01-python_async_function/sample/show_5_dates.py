import asyncio
import datetime


def display_date(cnt=5):
    print(datetime.datetime.now())
    cnt -= 1
    if cnt:
        loop.call_later(1, display_date, cnt)
    else:
        loop.stop()


loop = asyncio.get_event_loop()
loop.call_soon(display_date)
loop.run_forever()  # interrupted by loop.stop()
