from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from api.routes import api_router 
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler"""
    # Startup
    print("�� Starting Ollama AI Agents API...")
    print("📚 API Documentation available at: http://localhost:8000/docs")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down Ollama AI Agents API...") 
    
# Create FastAPI app
app = FastAPI(
    title="Ollama AI Agents API",
    description="FastAPI backend for CrewAI agents with Ollama integration",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 