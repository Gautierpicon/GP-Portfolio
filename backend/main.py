from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import httpx
import json

app = FastAPI()

OLLAMA_HOST = "http://localhost:11434"
OLLAMA_MODEL = "gemma3:1b"
ALLOWED_ORIGINS = ["http://localhost:4321"]
PORT = 8000

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

async def generate_response(message: str):
    try:
        async with httpx.AsyncClient() as client:
            async with client.stream(
                'POST',
                f'{OLLAMA_HOST}/api/generate',
                json={
                    'model': OLLAMA_MODEL,
                    'prompt': message,
                    'stream': True
                },
                timeout=60.0
            ) as response:
                if response.status_code != 200:
                    yield json.dumps({"error": f"Ollama error: {response.status_code}"})
                    return
                
                async for line in response.aiter_lines():
                    if line:
                        data = json.loads(line)
                        if 'response' in data:
                            yield data['response']
    
    except httpx.HTTPError as e:
        yield json.dumps({"error": f"Failed to connect to Ollama: {str(e)}"})
    except Exception as e:
        yield json.dumps({"error": str(e)})

@app.post("/api/chat")
async def chat(request: ChatRequest):
    """Endpoint chat qui retourne un stream"""
    return StreamingResponse(
        generate_response(request.message),
        media_type="text/event-stream"
    )

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "ollama_host": OLLAMA_HOST,
        "model": OLLAMA_MODEL
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)