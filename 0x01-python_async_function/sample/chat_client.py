import asyncio

HOST = 'localhost'
PORT = 8888


class EchoClientProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        print("Connected")
        transport.write(b"soy un cliente")

    def data_received(self, data):
        print('Received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('Server closed the connection')
        loop.stop()


loop = asyncio.get_event_loop()
coro = loop.create_connection(EchoClientProtocol, HOST, PORT)
loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
loop.close()
