#!/bin/bash

python3 -m llama_cpp.server \
  --model /gemma-3-27B-it-QAT-Q4_0.gguf \
  --host 0.0.0.0 \
  --port 8000 \
  --n_gpu_layers 1000 \
  --n_ctx 4096
  --use_mlock=True