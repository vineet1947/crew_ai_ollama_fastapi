# Ollama AI Agents - FastAPI Backend

A FastAPI backend for CrewAI agents with Ollama integration, providing a RESTful API for AI-powered research and content creation workflows.

## 🚀 Features

- **FastAPI Backend**: Modern, fast web framework with automatic API documentation
- **CrewAI Integration**: Multi-agent workflows for research and content creation
- **Ollama Support**: Local LLM integration with various models
- **RESTful API**: Clean API endpoints for easy integration
- **Health Monitoring**: Built-in health checks and status monitoring
- **Async Support**: Non-blocking operations for better performance

## 📁 Project Structure

```
ollama-ai-agents/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application
│   ├── api/
│   │   ├── __init__.py
│   │   ├── models.py           # Pydantic models
│   │   └── routes.py           # API routes
│   ├── agents/
│   │   ├── __init__.py
│   │   └── research_agents.py  # Agent definitions
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── research_tasks.py   # Task definitions
│   ├── services/
│   │   ├── __init__.py
│   │   └── crew_service.py     # Business logic
│   └── models/
│       ├── __init__.py
│       └── ollama_llm.py       # LLM configuration
├── run_server.py               # Server runner
├── requirements.txt            # Dependencies
├── pyproject.toml             # Project configuration
└── README.md                  # This file
```

## 🛠️ Installation

### Prerequisites

1. **Python 3.13+** installed
2. **Ollama** installed and running locally
3. **DeepSeek model** pulled in Ollama

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ollama-ai-agents
   ```

2. **Install dependencies**:
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # Or using uv (recommended)
   uv sync
   ```

3. **Setup Ollama**:
   ```bash
   # Install Ollama (if not already installed)
   # Visit: https://ollama.ai/
   
   # Pull the DeepSeek model
   ollama pull deepseek-r1:1.5b
   
   # Start Ollama (if not running)
   ollama serve
   ```

## 🚀 Running the Server

### Development Mode

```bash
# Run the FastAPI server
python run_server.py

# Or directly with uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Production Mode

```bash
# Run without reload for production
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The server will start on `http://localhost:8000`

## 📚 API Documentation

Once the server is running, you can access:

- **Interactive API Docs**: http://localhost:8000/docs (Swagger UI)
- **Alternative API Docs**: http://localhost:8000/redoc (ReDoc)
- **Health Check**: http://localhost:8000/api/v1/health

## 🔌 API Endpoints

### Base URL: `http://localhost:8000/api/v1`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information |
| `/health` | GET | Health status and Ollama availability |
| `/research` | POST | Execute research workflow |
| `/models` | GET | Available models information |

### Example Usage

#### Health Check
```bash
curl http://localhost:8000/api/v1/health
```

#### Research Workflow
```bash
curl -X POST "http://localhost:8000/api/v1/research" \
     -H "Content-Type: application/json" \
     -d '{"topic": "artificial intelligence trends 2024"}'
```

#### Python Example
```python
import requests

# Health check
response = requests.get("http://localhost:8000/api/v1/health")
print(response.json())

# Research workflow
data = {"topic": "artificial intelligence trends 2024"}
response = requests.post("http://localhost:8000/api/v1/research", json=data)
result = response.json()
print(result["result"])
```

## 🤖 Agents and Workflows

The system uses three specialized agents:

1. **Research Analyst**: Conducts thorough research on topics
2. **Content Writer**: Creates engaging content from research
3. **Content Editor**: Reviews and improves content quality

### Workflow Process

1. **Research Phase**: Agent analyzes the topic and gathers information
2. **Writing Phase**: Agent creates structured content based on research
3. **Editing Phase**: Agent polishes and improves the final content

## ⚙️ Configuration

### Ollama Model Configuration

Edit `app/models/ollama_llm.py` to change the default model:

```python
# Change the default model
ollama_llm = OllamaLLM(model_name="llama3.2:7b")
```

### Supported Models

- `deepseek-r1:1.5b` (default)
- `llama3.2:1b`
- `llama3.2:3b`
- `llama3.2:7b`
- `llama3.2:70b`

## 🔧 Development

### Adding New Agents

1. Create agent functions in `app/agents/`
2. Add corresponding tasks in `app/tasks/`
3. Update the service in `app/services/`
4. Add API endpoints in `app/api/routes.py`

### Adding New Workflows

1. Define workflow tasks in `app/tasks/`
2. Create workflow service methods in `app/services/crew_service.py`
3. Add API endpoints for the new workflow

## 🐛 Troubleshooting

### Common Issues

1. **Ollama Connection Error**:
   - Ensure Ollama is running: `ollama serve`
   - Check if the model is pulled: `ollama list`
   - Verify the model name in configuration

2. **Port Already in Use**:
   - Change the port in `run_server.py` or use a different port
   - Kill existing processes using the port

3. **Dependency Issues**:
   - Update dependencies: `pip install -r requirements.txt --upgrade`
   - Check Python version compatibility

### Debug Mode

Run with debug logging:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --log-level debug
```

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For issues and questions:
- Check the troubleshooting section
- Review API documentation at `/docs`
- Open an issue on GitHub
