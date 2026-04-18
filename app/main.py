from fastapi import FastAPI
from pydantic import BaseModel
from app.ingestion.embedder import Embedder
from app.retrieval.vector_store import VectorStore
from app.retrieval.retriever import Retriever
from app.retrieval.query_rewriter import rewrite_query
from app.retrieval.reranker import rerank
from app.llm.generator import generate_answer
from app.config import *
from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_text
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QueryRequest(BaseModel):
    query: str

app = FastAPI()

embedder = Embedder(EMBEDDING_MODEL)
vector_store = VectorStore(dim=384)  # MiniLM dim

# Load existing index if available
if os.path.exists(FAISS_INDEX_PATH):
    vector_store.load(FAISS_INDEX_PATH)

retriever = Retriever(vector_store, embedder)

@app.post("/ingest")
def ingest():
    files = os.listdir(DATA_PATH)
    for file in files:
        if file.endswith('.pdf'):
            text = load_pdf(os.path.join(DATA_PATH, file))
            chunks = chunk_text(text)
            embeddings = embedder.encode(chunks)
            vector_store.add(embeddings, chunks)
    
    os.makedirs(os.path.dirname(FAISS_INDEX_PATH), exist_ok=True)
    vector_store.save(FAISS_INDEX_PATH)
    return {"status": "ingested", "files_processed": len([f for f in files if f.endswith('.pdf')])}

@app.post("/query")
def query_api(request: QueryRequest):
    query = request.query
    logger.info(f"Processing query: {query}")
    rewritten = rewrite_query(query)

    docs = retriever.retrieve(rewritten, TOP_K)
    ranked_docs = rerank(query, docs)

    context = "\n".join(ranked_docs)

    answer = generate_answer(query, context)

    logger.info(f"Generated answer for query: {query[:50]}...")
    return {
        "query": query,
        "answer": answer,
        "sources": ranked_docs
    }
