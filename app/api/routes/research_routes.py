from fastapi import APIRouter, HTTPException
from api.models import ResearchRequest, ResearchResponse
from services.crew_service import crew_service

router = APIRouter()

@router.post("/", response_model=ResearchResponse)
async def execute_research(request: ResearchRequest):
    """Execute research workflow for a given topic"""
    try:
        result = await crew_service.execute_research_workflow(request.topic)
        return ResearchResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))