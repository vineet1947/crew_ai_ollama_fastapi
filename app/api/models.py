from pydantic import BaseModel, Field
from typing import Optional

class ResearchRequest(BaseModel):
    """Request model for research workflow"""
    topic: str = Field(..., description="The topic to research and write about", min_length=1, max_length=500)
    
class ResearchResponse(BaseModel):
    """Response model for research workflow"""
    success: bool
    error: Optional[str] = None
    result: Optional[str] = None
    topic: str
    
class HealthResponse(BaseModel):
    """Response model for health check"""
    status: str
    ollama_available: bool
    model: Optional[str] = None 