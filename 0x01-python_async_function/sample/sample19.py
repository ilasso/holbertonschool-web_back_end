#!/usr/bin/env python3
"""
as_completed() es un generador que administra la ejecución
de una lista de co-rutinas que se le dan y produce sus resultados
uno por uno a medida que terminan de correr. Al igual que con wait(),
el orden no es garantizado por as_completed(), pero no es necesario
esperar para que todas las operaciones en segundo plano se completen
antes de tomar otra acción.

Este ejemplo inicia varias fases de segundo plano que terminan
en el orden inverso en el que comienzan. A medida que se consume
el generador, el bucle espera el resultado de la rutina usando await.
https://rico-schmidt.name/pymotw-3/asyncio

"""
import asyncio


async def phase(i):
    print('in phase {}'.format(i))
    await asyncio.sleep(0.5 - (0.1 * i))
    print('done with phase {}'.format(i))
    return 'phase {} result'.format(i)


async def main(num_phases):
    print('starting main')
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print('waiting for phases to complete')
    results = []
    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print('received answer {!r}'.format(answer))
        results.append(answer)
    print('results: {!r}'.format(results))
    return results


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()
