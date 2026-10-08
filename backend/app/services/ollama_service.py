import httpx


OLLAMA_URL = "http://127.0.0.1:11434"


async def get_ollama_status():
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(f"{OLLAMA_URL}/api/tags")

    response.raise_for_status()

    return response.json()
