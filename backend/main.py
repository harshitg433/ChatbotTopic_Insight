# backend/main.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize Groq client
try:
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")
    groq_client = Groq(api_key=groq_api_key)
except Exception as e:
    print(f"Error initializing Groq client: {e}")
    groq_client = None # Set to None if initialization fails

# Pydantic model for request body
class PromptRequest(BaseModel):
    prompt: str

@app.post("/analyze_topic/")
async def analyze_topic(request: PromptRequest):
    """
    Receives a prompt, sends it to Groq LLM, and returns the response.
    """
    if not groq_client:
        raise HTTPException(status_code=500, detail="LLM service not available. GROQ_API_KEY might be missing or invalid.")

    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Analyze the following topic and provide a brief overview: {request.prompt}",
                }
            ],
            model="llama3-8b-8192", # Using a common Groq model, adjust if needed
            temperature=0.7,
            max_tokens=150,
        )
        llm_response = chat_completion.choices[0].message.content
        return {"response": llm_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting response from LLM: {e}")

# To run this backend:
# 1. Navigate to the 'backend' directory in your terminal.
# 2. Run: uvicorn main:app --reload --port 8000