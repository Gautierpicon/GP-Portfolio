# Backend - Portfolio

FastAPI backend that serves as a proxy between the frontend and a local Ollama AI instance.

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **AI Engine**: [Ollama](https://ollama.ai/)
- **Server**: [Uvicorn](https://www.uvicorn.org/)
- **HTTP Client**: [httpx](https://www.python-httpx.org/)
- **Environment Management**: [python-dotenv](https://pypi.org/project/python-dotenv/)
- **Hosting**: Self-hosted

## Project Structure

```
backend/
├── main.py              # Main FastAPI application
├── pyproject.toml       # Project configuration and dependencies
├── .env                 # Environment variables (not tracked by git)
└── README.md
```

## Installation

### Prerequisites

- Python 3.9+
- [uv](https://docs.astral.sh/uv/) package manager
- [Ollama](https://ollama.ai/) installed and running locally
- An Ollama model pulled (e.g., `ollama pull gemma3:1b`)

### Steps

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies
```bash
uv sync
```

3. **Create your `.env` file:**
```bash
cp .env.example .env
```

Edit `.env`:

Example `.env` for **local development**:
```dotenv
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma3:1b
ALLOWED_ORIGINS=http://localhost:4321
PORT=8000
```

Example `.env` for **production**:
```dotenv
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma3:1b
ALLOWED_ORIGINS=https://gautierpicon.com/
PORT=8000
```

4. Custom model configuration

To set up the custom model, go to the dedicated [README.md](../DuckAI/README.md) file for the model.

5. Start the server:
```bash
uv run uvicorn main:app --reload --port 8000
```

The API will be accessible at `http://localhost:8000`

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OLLAMA_HOST` | URL of the Ollama instance | `http://localhost:11434` |
| `OLLAMA_MODEL` | Ollama model to use | `gemma3:1b` |
| `ALLOWED_ORIGINS` | CORS allowed origins (comma-separated) | `http://localhost:4321` |
| `PORT` | Server port | `8000` |

### Multiple Origins

To allow multiple origins (e.g., local dev + production), use comma-separated values:

```dotenv
ALLOWED_ORIGINS=http://localhost:4321,https://gautierpicon.com/
```

## API Documentation

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
  "model": "DuckAI"
}
```

**Example with curl:**
```bash
curl http://localhost:8000/health
```


## Ollama Integration

The backend streams the Ollama response with:

```python
client.stream(
    'POST',
    f'{OLLAMA_HOST}/api/generate',
    json={
        'model': OLLAMA_MODEL,
        'prompt': message,
        'stream': True
    }
)
```
The stream is then sent back to the frontend via StreamingResponse

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | 0.121.0 | Web framework |
| `uvicorn[standard]` | 0.32.1 | ASGI server |
| `httpx` | 0.28.1 | Async HTTP client |
| `pydantic` | 2.10.3 | Data validation |
| `python-dotenv` | 1.0.1 | Environment variables management |

## Feedback

Feedback are welcome! Feel free to open an [issue](https://github.com/Gautierpicon/GP-Portfolio/issues) or a [pull request](https://github.com/Gautierpicon/GP-Portfolio/pulls) on the GitHub repository.