import asyncio

HOST = 'localhost'
PORT = 8888


class EchoClientProtocol(asyncio.Protocol):

    def __init__(self):
        super().__init__()
        self.transport = None

    def send(self, text):
        if self.transport is not None:
            self.transport.write(text.encode('utf8'))

    def connection_made(self, transport):
        print("Connected")
        self.transport = transport

    def data_received(self, data):
        print("<--", data.decode())

    def connection_lost(self, exc):
        print('Server closed the connection')
        self.transport = None


async def user_input(queue):
    while True:
        text = await loop.run_in_executor(None, input, "--> ")
        await queue.put(text)


async def main():
    _, protocol = await loop.create_connection(EchoClientProtocol, HOST, PORT)
    queue = asyncio.Queue()
    loop.create_task(user_input(queue))
    while True:
        text = await queue.get()
        protocol.send(text)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
except KeyboardInterrupt:
    pass
loop.close()
