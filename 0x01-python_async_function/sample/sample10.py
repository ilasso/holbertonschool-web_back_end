#!/usr/bin/env python3
"""
Un Future también se puede usar con la palabra clave await, como en este ejemplo.

El resultado de Future es devuelto por await, por lo que es con frecuencia es
posible tener el mismo código de trabajo con una co-rutina normal y una instancia
Future.
"""
import asyncio


def mark_done(future, result):
    print('setting future result to {!r}'.format(result))
    future.set_result(result)


async def main(loop):
    all_done = asyncio.Future()

    print('scheduling mark_done')
    loop.call_soon(mark_done, all_done, 'the result')

    result = await all_done
    print('returned result: {!r}'.format(result))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
