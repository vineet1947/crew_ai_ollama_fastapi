from fastapi import APIRouter
from .health_routes import router as health_router
from .research_routes import router as research_router
from .models_routes import router as models_router

# Create main API router
api_router = APIRouter()

# Include all route modules with their prefixes
api_router.include_router(health_router, prefix="/health", tags=["health"])
api_router.include_router(research_router, prefix="/research", tags=["research"])
api_router.include_router(models_router, prefix="/models", tags=["models"])

# Root endpoint
@api_router.get("/", response_model=dict)
async def root():
    """Root endpoint"""
    return {
        "message": "Ollama AI Agents API",
        "version": "1.0.0",
        "description": "FastAPI backend for CrewAI agents with Ollama integration"
    }