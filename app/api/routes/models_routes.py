from fastapi import APIRouter
from services.crew_service import crew_service

router = APIRouter()

@router.get("/")
async def get_available_models():
    """Get information about available models"""
    return {
        "current_model": crew_service.llm.model if crew_service.llm else None,
        "ollama_available": crew_service.is_ollama_available(),
        "supported_models": [
            "deepseek-r1:1.5b",
            "qwen3:0.6b"
        ]
    }