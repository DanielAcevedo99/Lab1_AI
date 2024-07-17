from fastapi import FastAPI, Body, Query
from typing import Optional
import google.generativeai as genai
from vertexai.preview import tokenization
from pydantic import BaseModel

API_KEY = "AIzaSyC5L93vD_yXeVTKg__v1YbhnXALYA3LgAw"

app = FastAPI()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

class TextRequest(BaseModel):
    text: str

def summarize_text(text: str) -> str:
    prompt = f"Summarize the next text: {text}"
    response = model.generate_content(prompt)
    summary = response.text

    if len(summary.split()) > 100:
        summary = ' '.join(summary.split()[:100]) + "..."

    return summary

def count_tokens(text: str) -> int:
    model_name = "gemini-1.5-flash-001"
    tokenizer = tokenization.get_tokenizer_for_model(model_name)
    result = tokenizer.count_tokens(text)
    return result.total_tokens

@app.post("/summarize")
async def summarize(request: TextRequest):
    summary = summarize_text(request.text)
    return {"summary": summary}

@app.get("/count-tokens")
async def count_tokns(text: str = Query(...)):
    token_count = count_tokens(text)
    return {"token_count": token_count}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
