import asyncio
import websockets
import json


class WebSocketServer:
    def __init__(self, host, port):
        self.clients = set()
        self.host = host
        self.port = port

    async def register(self, websocket):
        self.clients.add(websocket)
        print(f"{websocket} connects.")

    async def unregister(self, websocket):
        self.clients.remove(websocket)
        print(f"{websocket} disconnects.")

    async def send_to_all(self, message):
        if self.clients:  # Check if there are any clients connected
            await asyncio.wait([client.send(message) for client in self.clients])

    async def handle_message(self, websocket, path):
        await self.register(websocket)
        try:
            async for message in websocket:
                data = json.loads(message)
                # Process the message
                print(f"Received message from {websocket}: {data}")
                # Here you can implement custom logic based on the message type or content

                response = json.dumps({"type": "echo", "data": data})
                await self.send_to_all(response)
        finally:
            await self.unregister(websocket)

    def run(self):
        start_server = websockets.serve(self.handle_message, self.host, self.port)
        asyncio.get_event_loop().run_until_complete(start_server)
        print(f"WebSocket Server running on ws://{self.host}:{self.port}")
        asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    server = WebSocketServer("localhost", 8765)
    server.run()
