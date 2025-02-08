from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import ollama
import logging
from typing import Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Br8niac Search API")

class SearchQuery(BaseModel):
    query: str

@app.get("/api/status")
async def get_status() -> Dict[str, Any]:
    try:
        # Check if Ollama is running and get model info
        models = ollama.list()
        return {
            "status": "online",
            "models": models
        }
    except Exception as e:
        logger.error(f"Error checking status: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get model status")

@app.post("/api/search")
async def search(query: SearchQuery) -> Dict[str, Any]:
    try:
        # Use Ollama to process the search query
        response = ollama.generate(
            model='mistral',  # You can change this to your preferred model
            prompt=f"Search query: {query.query}\nPlease provide relevant information.",
            stream=False
        )
        
        return {
            "query": query.query,
            "results": response['response']
        }
    except Exception as e:
        logger.error(f"Error processing search: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process search query")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)