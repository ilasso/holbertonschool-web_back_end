#!/usr/bin/env python3
"""
se programa el callback/funcion para un momento especifico dentro
del bucle
"""

import asyncio
import time


def callback(n, loop):
    print('callback {} invoked at {}'.format(n, loop.time()))


async def main(loop):
    now = loop.time()
    print('clock time: {}'.format(time.time()))
    print('loop  time: {}'.format(now))

    print('registering callbacks')
    loop.call_at(now + 0.2, callback, 1, loop)
    loop.call_at(now + 0.4, callback, 2, loop)
    loop.call_soon(callback, 3, loop)

    await asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
    #print(event_loop.__dict__)
    #print(dir(event_loop))
    #print(event_loop._scheduled)
finally:
    print('closing event loop')
    event_loop.close()