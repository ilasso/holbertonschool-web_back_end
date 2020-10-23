#!/usr/bin/env python3
"""
Un Futuro representa el resultado de un trabajo que no ha sido
completado aún. El bucle de eventos puede seguir el estado de
un objeto Future para indicar que está listo, permitiendo que
una parte de una aplicación espere otra parte para terminar un trabajo.

Un Future actúa como una co-rutina, por lo que cualquier
técnica útil para esperar a una co-rutina también puede usarse
para esperar que el futuro sea marcado como listo.
Este ejemplo pasa el futuro al método run_until_complete()
del bucle de eventos.
"""

import asyncio


def mark_done(future, result):
    print('setting future result to {!r}'.format(result))
    future.set_result(result)


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()

    print('scheduling mark_done')
    event_loop.call_soon(mark_done, all_done, 'the result')

    print('entering event loop')
    result = event_loop.run_until_complete(all_done)
    print('returned result: {!r}'.format(result))
finally:
    print('closing event loop')
    event_loop.close()

print('future result: {!r}'.format(all_done.result()))
