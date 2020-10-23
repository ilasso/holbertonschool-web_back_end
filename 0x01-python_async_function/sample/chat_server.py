
import asyncio

HOST = 'localhost'
PORT = 8888


class ChatServerProtocol(asyncio.Protocol):

    clients = []

    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        print('Connection from {}'.format(transport.get_extra_info('peername')))
        self.transport = transport
        self.clients.append(transport)

    def connection_lost(self, reason):
        self.clients.remove(self.transport)

    def data_received(self, data):
        print('Data received: {!r}'.format(data))
        for transport in self.clients:
            if transport is not self.transport:
                transport.write(data)


loop = asyncio.get_event_loop()
# Each client connection will create a new protocol instance
coro = loop.create_server(ChatServerProtocol, HOST, PORT)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
