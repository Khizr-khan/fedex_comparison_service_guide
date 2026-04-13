#!/bin/bash
# Downloads both ChromaDBs from HuggingFace datasets at container start.
# HF_TOKEN is only available at runtime (not Docker build time).

python -c "
import os
from huggingface_hub import snapshot_download

token = os.environ.get('HF_TOKEN')

print('Downloading 2026 DB...')
snapshot_download(
    repo_id='Khizr72/fedex-service-guide',
    repo_type='dataset',
    local_dir='./chroma_fedex_db',
    token=token,
)

print('Downloading 2025 DB...')
snapshot_download(
    repo_id='Khizr72/fedex-service-guide-2025',
    repo_type='dataset',
    local_dir='./chroma_fedex_db_2025',
    token=token,
)

print('Both DBs ready.')
"

uvicorn main:app --host 0.0.0.0 --port 7860