FROM nvidia/cuda:12.9.0-devel-ubuntu22.04

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    git \
    cmake \
    curl \
    python3 \
    libcurl4 \
    && rm -rf /var/lib/apt/lists/*

# Клонирование и сборка (последняя версия)
RUN git clone https://github.com/ggerganov/llama.cpp && \
    cd llama.cpp && \
    mkdir build && \
    cd build && \
    cmake .. -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES="89" -DLLAMA_CURL=OFF && \
    cmake --build . --config Release --target server --parallel $(nproc)

# Настройка окружения
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64
WORKDIR /app
VOLUME /app/models

EXPOSE 8080

CMD ["/llama.cpp/build/bin/server", \
    "-m", "/app/models/gemma-3-27B-it-QAT-Q4_0.gguf", \
    "--n-gpu-layers", "40", \
    "--host", "0.0.0.0", \
    "--port", "5001"]