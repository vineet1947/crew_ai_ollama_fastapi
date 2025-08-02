from crewai import LLM
import os
from typing import Optional

class OllamaLLM:
    """Ollama LLM configuration and setup"""
    
    def __init__(self, model_name: str = "deepseek-r1:1.5b", base_url: str = "http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
        self._llm_instance: Optional[LLM] = None
    
    def setup_llm(self) -> Optional[LLM]:
        """Setup and return Ollama LLM instance"""
        try:
            self._llm_instance = LLM(
                model=f"ollama/{self.model_name}",
                base_url=self.base_url
            )
            print(f"✅ Successfully connected to Ollama with {self.model_name} model")
            return self._llm_instance
        except Exception as e:
            print(f"❌ Error connecting to Ollama: {e}")
            print(f"Make sure Ollama is running with: ollama run {self.model_name}")
            return None
    
    def get_llm(self) -> Optional[LLM]:
        """Get the LLM instance, setup if not already done"""
        if self._llm_instance is None:
            return self.setup_llm()
        return self._llm_instance
    
    def is_available(self) -> bool:
        """Check if Ollama LLM is available"""
        return self.get_llm() is not None

# Factory functions for different models
def create_llm(model_name: str = "deepseek-r1:1.5b", base_url: str = "http://localhost:11434") -> Optional[LLM]:
    """Create a new LLM instance with specified model"""
    ollama = OllamaLLM(model_name, base_url)
    return ollama.get_llm()

def create_deepseek_llm() -> Optional[LLM]:
    """Create LLM instance with DeepSeek model"""
    return create_llm("deepseek-r1:1.5b")

def create_qwen_llm() -> Optional[LLM]:
    """Create LLM instance with Qwen model"""
    return create_llm("qwen3:0.6b") 

# Default global instance (for backward compatibility)
ollama_llm = OllamaLLM() 