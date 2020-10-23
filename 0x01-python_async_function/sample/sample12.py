#!/usr/bin/env python3
"""
Para iniciar una tarea, usa create_task()
para crear una instancia Task. La tarea resultante se ejecutará
como parte de las operaciones simultáneas gestionadas por el
bucle de eventos siempre que el bucle esté corriendo
y la co-rutina no retorne.
Este ejemplo espera a que la tarea devuelva
un resultado antes de que la función main() termine.
"""
import asyncio


async def task_func():
    print('in task_func')
    return 'the result'


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    print('waiting for {!r}'.format(task))
    return_value = await task
    print('task completed {!r}'.format(task))
    print('return value: {!r}'.format(return_value))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
