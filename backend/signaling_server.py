import asyncio
import json
import websockets

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            for client in connected_clients:
                if client != websocket:
                    await client.send(json.dumps(data))
    finally:
        connected_clients.remove(websocket)

start_server = websockets.serve(handler, "0.0.0.0", 8765)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

