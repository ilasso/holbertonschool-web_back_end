#!/usr/bin/env python3
"""
Si las fases de segundo plano están bien definidas,
y solo los resultados de esas fases son importantes,
entonces gather() puede ser más útil para esperar múltiples operaciones.

Las tareas creadas por gather no son expuestas, por lo que no pueden
ser canceladas. El valor de retorno es una lista de resultados en el
mismo orden que los argumentos pasados a gather(), independientemente
del orden en que las operaciones de segundo plano son completadas.
https://rico-schmidt.name/pymotw-3/asyncio
"""
import asyncio


async def phase1():
    print('in phase1')
    await asyncio.sleep(2)
    print('done with phase1')
    return 'phase1 result'


async def phase2():
    print('in phase2')
    await asyncio.sleep(1)
    print('done with phase2')
    return 'phase2 result'


async def main():
    print('starting main')
    print('waiting for phases to complete')
    results = await asyncio.gather(
        phase1(),
        phase2(),
    )
    print('results: {!r}'.format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main())
finally:
    event_loop.close()
