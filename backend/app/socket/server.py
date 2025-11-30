import asyncio
import socketio

sio = socketio.AsyncServer(async_mode="asgi")
socket_app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print(f"[socket] connect: {sid}")

@sio.event
async def disconnect(sid):
    print(f"[socket] disconnect: {sid}")

@sio.event
async def start_reasoning(sid, data):
    print(f"[socket] start_reasoning from {sid}: {data}")
    await sio.emit('agent_update', {'agent': 'lyra-agent', 'status': 'started'}, to=sid)
    await asyncio.sleep(0.4)
    await sio.emit('agent_update', {'agent': 'lyra-agent', 'status': 'working'}, to=sid)
    await asyncio.sleep(0.6)
    await sio.emit('agent_update', {'agent': 'lyra-agent', 'status': 'done'}, to=sid)
