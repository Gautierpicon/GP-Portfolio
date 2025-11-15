# Backend - Portfolio

FastAPI backend that serves as a proxy between the frontend and a local Ollama AI instance.

## 🚀 Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **AI Engine**: [Ollama](https://ollama.ai/)
- **Server**: [Uvicorn](https://www.uvicorn.org/)
- **HTTP Client**: [httpx](https://www.python-httpx.org/)
- **Hosting**: Self-hosted (Raspberry Pi)

## 📁 Project Structure

```
backend/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in repo)
├── .gitignore
└── README.md
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running locally
- An Ollama model pulled (e.g., `ollama pull gemma3:1b`)

### Steps

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python3 -m venv venv
```

3. Activate the virtual environment:
```bash
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file at the root of the backend folder:
```bash
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma3:1b
ALLOWED_ORIGINS=http://localhost:4321,https://frontend.com
PORT=8000
```

6. Start the server:
```bash
uvicorn main:app --reload --port 8000
```

The API will be accessible at `http://localhost:8000`

## 🔧 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `OLLAMA_HOST` | URL of the Ollama instance | `http://localhost:11434` |
| `OLLAMA_MODEL` | Name of the Ollama model to use | `llama2` or `mistral` |
| `ALLOWED_ORIGINS` | Comma-separated list of allowed CORS origins | `http://localhost:4321,https://example.com` |
| `PORT` | Port on which the server runs | `8000` |

## 📡 API Documentation

### Endpoints

#### `POST /api/chat`

Sends a message to the Ollama AI and returns the response.

**Request Body:**
```json
{
  "message": "string"
}
```

**Response:**
```json
{
  "response": "string"
}
```

**Example with curl:**
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, who are you?"}'
```

**Example Response:**
```json
{
  "response": "I am an AI assistant. How can I help you today?"
}
```

**Error Responses:**

- `500` - Failed to connect to Ollama or internal server error
```json
{
  "detail": "Failed to connect to Ollama: Connection refused"
}
```

---

#### `GET /health`

Health check endpoint to verify the API is running and properly configured.

**Response:**
```json
{
  "status": "ok",
  "ollama_host": "http://localhost:11434",
  "model": "gemma3:1b"
}
```

**Example with curl:**
```bash
curl http://localhost:8000/health
```

---

### Interactive Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

These interfaces allow you to test the API directly from your browser.

## 🔒 CORS Configuration

The API uses CORS middleware to allow requests from authorized origins only. Origins are configured via the `ALLOWED_ORIGINS` environment variable.

```python
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🤖 Ollama Integration

The backend communicates with Ollama via its REST API:

1. The frontend sends a message to `/api/chat`
2. The backend forwards the request to Ollama at `{OLLAMA_HOST}/api/generate`
3. Ollama processes the request with the configured model
4. The backend returns the AI's response to the frontend

**Ollama API Call:**
```python
ollama_response = await client.post(
    f'{OLLAMA_HOST}/api/generate',
    json={
        'model': OLLAMA_MODEL,
        'prompt': request.message,
        'stream': False
    },
    timeout=60.0
)
```

## 📊 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | ≥0.115.0 | Web framework |
| `uvicorn[standard]` | ≥0.32.0 | ASGI server |
| `httpx` | ≥0.27.0 | Async HTTP client |
| `pydantic` | ≥2.10.0 | Data validation |
| `python-dotenv` | 1.0.0 | Environment variables |

## 🤝 Feedback

Feedback are welcome! Feel free to open an [issue](https://github.com/Gautierpicon/Portfolio/issues) or a [pull request](https://github.com/Gautierpicon/Portfolio/pulls) on the GitHub repository.

## 🔗 Useful Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Frontend README](../frontend/README.md)