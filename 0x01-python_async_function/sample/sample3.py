#!/usr/bin/env python3
"""
Bucle de eventos simple
instancia un bucle de eventos y ejecuta una corutina hasta que termine
la corutina retorna un valor
"""

import asyncio


async def coroutine():
    print('in coroutine')
    return "result"


event_loop = asyncio.get_event_loop()
try:
    print('starting coroutine')
    coro = coroutine()
    print('entering event loop')
    return_value = event_loop.run_until_complete(coro)
    print('it returned: {!r}'.format(return_value))
finally:
    print('closing event loop')
    event_loop.close()
