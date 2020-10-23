#!/usr/bin/env python3
"""
A menudo es útil dividir una operación en muchas partes
y ejecutarlas por separado. Por ejemplo, descargar varios
recursos remotos o consultar interfaces de programación remotas.
En situaciones donde el orden de ejecución no importa, y donde
puede haber un número arbitrario de operaciones, wait() se puede usar
para pausar una co-rutina hasta que otras operaciones de segundo plano
sean completadas.

Internamente, wait() usa un set para mantener la instancia Task que crea.
Esto hace que comiencen y terminen en un orden impredecible.
El valor de retorno de wait() es una tupla que contiene dos conjuntos que
contienen las tareas terminadas y pendientes.
https://rico-schmidt.name/pymotw-3/asyncio

"""
import asyncio


async def phase(i):
    print('in phase {}'.format(i))
    await asyncio.sleep(0.1 * i)
    print('done with phase {}'.format(i))
    return 'phase {} result'.format(i)


async def main(num_phases):
    print('starting main')
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print('waiting for phases to complete')
    completed, pending = await asyncio.wait(phases)
    results = [t.result() for t in completed]
    print('results: {!r}'.format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()
