from fastapi import FastAPI
from backend.app.api.ollama import router as ollama_router

app = FastAPI(
    title="Assistant Valix AI",
    description="AI Customer Care Assistant",
    version="0.1.0"
)


app.include_router(
    ollama_router,
    prefix="/api/ollama",
    tags=["Ollama"]
)


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "Assistant Valix AI"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
