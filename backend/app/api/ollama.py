from fastapi import APIRouter
from backend.app.services.ollama_service import get_ollama_status

router = APIRouter()


@router.get("/status")
async def ollama_status():
    try:
        data = await get_ollama_status()

        return {
            "status": "online",
            "models": data.get("models", [])
        }

    except Exception as e:
        return {
            "status": "offline",
            "error": str(e)
        }
