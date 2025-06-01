from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llama_cpp import Llama
import os

app = FastAPI()

# Настройки CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Загрузка модели
model_path = "/models/gemma-3-27B-it-QAT-Q4_0.gguf"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

llm = Llama(
    model_path=model_path,
    n_gpu_layers=-1,  # Использовать все слои на GPU
    n_ctx=4096,       # Размер контекста
    n_batch=512,      # Размер батча
)

class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 256
    temperature: float = 0.7
    top_p: float = 0.9

@app.post("/generate")
async def generate_text(request: PromptRequest):
    output = llm.create_completion(
        prompt=request.prompt,
        max_tokens=request.max_tokens,
        temperature=request.temperature,
        top_p=request.top_p,
        echo=False,
        stream=False
    )
    return {"response": output["choices"][0]["text"]}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}