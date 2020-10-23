#!/usr/bin/env python3
"""
Además de trabajar como una co-rutina,
un Future puede invocar calbacks cuando se completa.
Las callbacks se invocan en el orden en que están registrados
La callback debe esperar un argumento, la instancia Future.
Para pasar argumentos adicionales a las calbacks,
use functools.partial() para crear un envoltorio.

"""
import asyncio
import functools


def callback(future, n):
    print('{}: future done: {}'.format(n, future.result()))


async def register_callbacks(all_done):
    print('registering callbacks on future')
    all_done.add_done_callback(functools.partial(callback, n=1))
    all_done.add_done_callback(functools.partial(callback, n=2))


async def main(all_done):
    await register_callbacks(all_done)
    print('setting result of future')
    all_done.set_result('the result')


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()
    event_loop.run_until_complete(main(all_done))
finally:
    event_loop.close()
