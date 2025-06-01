import os

# Настройки модели
MODEL_CONFIG = {
    "model_path": os.getenv("MODEL_PATH", "/models/gemma-2b-it-Q4_0.gguf"),
    "gpu_layers": int(os.getenv("GPU_LAYERS", 20)),  # Количество слоев на GPU
    "batch_size": int(os.getenv("BATCH_SIZE", 4)),   # Размер батча
    "context_size": int(os.getenv("CONTEXT_SIZE", 2048)),  # Длина контекста
    "threads": int(os.getenv("NUM_THREADS", 8)),     # Количество потоков CPU
}

# Настройки API
API_CONFIG = {
    "host": "0.0.0.0",
    "port": int(os.getenv("PORT", 5001)),
    "debug": os.getenv("DEBUG", "false").lower() == "true"
}

# Настройки генерации
GENERATION_CONFIG = {
    "temperature": 0.7,
    "top_p": 0.9,
    "max_length": 50,
    "repetition_penalty": 1.1
}