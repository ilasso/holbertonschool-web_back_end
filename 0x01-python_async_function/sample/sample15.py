#!/usr/bin/env python3
"""
La función ensure_future() devuelve una Task vinculada
a la ejecución de una co-rutina.
Esa instancia Task puede entonces ser pasada a otro código,
que puede esperarla sin saber cómo la co-rutina original
fue construida o llamada.
Ten en cuenta que la rutina asignada a ensure_future()
no se inicia hasta que algo use await para permitir que se ejecute.
https://rico-schmidt.name/pymotw-3/asyncio
"""
import asyncio


async def wrapped():
    print('wrapped')
    return 'result'


async def inner(task):
    print('inner: starting')
    print('inner: waiting for {!r}'.format(task))
    result = await task
    print('inner: task returned {!r}'.format(result))
    print('inner: waiting for {!r}'.format(task))


async def starter():
    print('starter: creating task')
    task = asyncio.ensure_future(wrapped())
    print('starter: waiting for inner')
    await inner(task)
    print('starter: inner returned')


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    result = event_loop.run_until_complete(starter())
finally:
    event_loop.close()
