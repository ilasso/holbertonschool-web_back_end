#!/usr/bin/env python3
"""
Al retener el objeto Task devuelto de create_task(),
es posible cancelar la operación de la tarea antes de que se complete.
Este ejemplo crea y luego cancela una tarea antes de iniciar
el bucle de eventos. El resultado es una excepción CancelledError
de run_until_complete().
"""
import asyncio


async def task_func():
    print('in task_func')
    return 'the result'


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())

    print('canceling task')
    task.cancel()

    print('canceled task {!r}'.format(task))
    try:
        await task
    except asyncio.CancelledError:
        print('caught error from canceled task')
        print('canceled task {!r}'.format(task))
    else:
        print('task result: {!r}'.format(task.result()))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
