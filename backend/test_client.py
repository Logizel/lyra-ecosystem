import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("✅ [Client] Connected to Lyra Backend!")
    
    task_payload = {'query': 'Build a Snake Game in Python'}
    print(f"🚀 [Client] Sending task: {task_payload['query']}")
    
    await sio.emit('start_reasoning', task_payload)

@sio.event
async def agent_update(data):
    agent_name = data.get('agent')
    status_msg = data.get('status')
    print(f"📩 [Client] Received Update from {agent_name}: {status_msg}")

@sio.event
async def disconnect():
    print("❌ [Client] Disconnected from server")

async def main():
    try:
        await sio.connect('http://localhost:8000')
        await sio.wait()
        
    except Exception as e:
        print(f"⚠️ Connection failed: {e}")
        print("Did you forget to start the server with 'uvicorn app.main:app --reload'?")

if __name__ == '__main__':
    asyncio.run(main())
