#!/usr/bin/env python3
"""llamdos a callbacks funciones regulares dentro del bucle
    call_soon es un metodo de la clase del loop
    este metodo programa la ejecucion en la proxima
    iteracion del bucle
    se usa functools.partial para poder pasar los kwargs
"""
import asyncio
import functools


def callback(arg, *, kwarg='default'):
    print('callback invoked with {} and {}'.format(arg, kwarg))


async def main(loop):
    print('registering callbacks')
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwarg='not default')
    loop.call_soon(wrapped, "2")

    await asyncio.sleep(0.1)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
