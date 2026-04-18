import os

DATA_PATH = "data/raw"
FAISS_INDEX_PATH = "data/processed/faiss_index"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "mistral"  # if using Ollama
TOP_K = 5
