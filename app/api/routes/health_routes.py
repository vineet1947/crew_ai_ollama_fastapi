from fastapi import APIRouter
from api.models import HealthResponse
from services.crew_service import crew_service

router = APIRouter()

@router.get("/", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return await crew_service.get_health_status()