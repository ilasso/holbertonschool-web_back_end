#!/usr/bin/env python3
"""
Solo quedarán operaciones pendientes si se usa wait()
con un valor de tiempo de espera.
Las operaciones de segundo plano restantes deben cancelarse
o ser terminadas al esperarlas. Dejándolos pendientes mientras
el bucle de eventos continúa les permitirá seguir ejecutándose,
lo que puede no ser deseable si la operación general se considera abortada.
Dejándolos pendiente al final del proceso resultará en advertencias que serán
reportadas.
https://rico-schmidt.name/pymotw-3/asyncio
"""
import asyncio


async def phase(i):
    print('in phase {}'.format(i))
    try:
        await asyncio.sleep(0.1 * i)
    except asyncio.CancelledError:
        print('phase {} canceled'.format(i))
        raise
    else:
        print('done with phase {}'.format(i))
        return 'phase {} result'.format(i)


async def main(num_phases):
    print('starting main')
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print('waiting 0.1 for phases to complete')
    completed, pending = await asyncio.wait(phases, timeout=0.1)
    print('{} completed and {} pending'.format(
        len(completed), len(pending),
    ))
    # Cancel remaining tasks so they do not generate errors
    # as we exit without finishing them.
    if pending:
        print('canceling tasks')
        for t in pending:
            t.cancel()
    print('exiting main')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()
