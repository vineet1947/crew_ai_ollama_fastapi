from fastapi import APIRouter, HTTPException
from api.models import ResearchRequest, ResearchResponse, HealthResponse
from services.crew_service import crew_service

router = APIRouter()

@router.get("/", response_model=dict)
async def root():
    """Root endpoint"""
    return {
        "message": "Ollama AI Agents API",
        "version": "1.0.0",
        "description": "FastAPI backend for CrewAI agents with Ollama integration"
    }

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return await crew_service.get_health_status()

@router.post("/research", response_model=ResearchResponse)
async def execute_research(request: ResearchRequest):
    """Execute research workflow for a given topic"""
    try:
        result = await crew_service.execute_research_workflow(request.topic)
        return ResearchResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models")
async def get_available_models():
    """Get information about available models"""
    return {
        "current_model": crew_service.llm.model if crew_service.llm else None,
        "ollama_available": crew_service.is_ollama_available(),
        "supported_models": [
            "deepseek-r1:1.5b",
            "llama3.2:1b",
            "llama3.2:3b",
            "llama3.2:7b",
            "llama3.2:70b"
        ]
    } 