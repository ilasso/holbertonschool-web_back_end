import asyncio

from socket import socketpair


def reader():
    data = rsock.recv(3)
    print("Received:", data)


rsock, wsock = socketpair()
loop = asyncio.get_event_loop()
loop.add_reader(rsock, reader)

loop.call_soon(wsock.send, b"foobardo")
loop.run_forever()
