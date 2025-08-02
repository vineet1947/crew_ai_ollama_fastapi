from crewai import Crew, Process
from models.ollama_llm import ollama_llm
from agents.research_agents import researcher_agent, writer_agent, editor_agent
from tasks.research_tasks import create_research_workflow_tasks
from typing import Optional, Dict, Any

class CrewService:
    """Service for managing CrewAI workflows"""
    
    def __init__(self):
        self.llm = ollama_llm.get_llm()
    
    def is_ollama_available(self) -> bool:
        """Check if Ollama is available"""
        return ollama_llm.is_available()
    
    async def execute_research_workflow(self, topic: str) -> Dict[str, Any]:
        """Execute the complete research workflow"""
        try:
            # Check if Ollama is available
            if not self.is_ollama_available():
                return {
                    "success": False,
                    "error": "Ollama is not available. Please make sure it's running.",
                    "result": None
                }
            
            # Use the pre-configured agents
            researcher, writer, editor = researcher_agent, writer_agent, editor_agent
            
            # Create tasks
            tasks = create_research_workflow_tasks(researcher, writer, editor, topic)
            
            # Create crew
            crew = Crew(
                agents=[researcher, writer, editor],
                tasks=tasks,
                verbose=True,
                process=Process.sequential
            )
            
            # Execute the crew
            crew_output = crew.kickoff()
            
            # Convert CrewOutput to string
            result_string = str(crew_output.raw) if hasattr(crew_output, 'raw') else str(crew_output)
            
            return {
                "success": True,
                "error": None,
                "result": result_string,
                "topic": topic
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "result": None,
                "topic": topic
            }
    
    async def get_health_status(self) -> Dict[str, Any]:
        """Get the health status of the service"""
        return {
            "status": "healthy" if self.is_ollama_available() else "unhealthy",
            "ollama_available": self.is_ollama_available(),
            "model": ollama_llm.model_name if self.is_ollama_available() else None
        }

# Global service instance
crew_service = CrewService() 