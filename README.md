# Personal AI Knowledge Vault

A **Retrieval-Augmented Generation (RAG)** system that ingests personal documents (PDFs) and enables natural language querying of a personal knowledge base using a local LLM.

## Features

- **Document Ingestion**: Upload and process PDF documents (medical reports, resumes, transcripts, journals, etc.)
- **Vector Search**: Semantic search using FAISS and Sentence Transformers embeddings
- **Local LLM**: Integrates with Ollama (Mistral) for privacy-preserving answer generation
- **Query Rewriting**: Enhances queries for better retrieval accuracy
- **Document Reranking**: Ranks retrieved documents for relevance
- **REST API**: FastAPI-powered endpoints for ingestion and querying
- **Persistent Storage**: Saves vector indices for efficient retrieval

## Tech Stack

- **Backend**: FastAPI, Uvicorn
- **AI/ML**: Sentence Transformers, FAISS, PyTorch
- **Document Processing**: PyPDF
- **LLM**: Ollama (Mistral)
- **Environment**: Python 3.9+, Virtual Environment

##  Project Structure

```
personal-ai-knowledge-vault/
├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── config.py            # Configuration (paths, model names)
│   ├── ingestion/
│   │   ├── loader.py        # PDF loading
│   │   ├── chunker.py       # Text chunking
│   │   └── embedder.py      # Embedding generation
│   ├── retrieval/
│   │   ├── vector_store.py  # FAISS vector store
│   │   ├── retriever.py     # Document retrieval
│   │   ├── reranker.py      # Document ranking
│   │   └── query_rewriter.py # Query enhancement
│   ├── llm/
│   │   └── generator.py     # LLM response generation
│   └── utils/
│       └── security.py      # Security utilities
├── data/
│   ├── raw/                 # Upload PDFs here
│   └── processed/           # Saved embeddings/index
├── requirements.txt
├── .gitignore
└── README.md
```

##  Setup

### Prerequisites
- Python 3.9+
- Ollama (download from [ollama.ai](https://ollama.ai))
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sahil860860/personal-ai-knowledge-vault.git
   cd personal-ai-knowledge-vault
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Ollama and download Mistral**
   ```bash
   ollama serve          # In one terminal
   ollama pull mistral   # In another terminal
   ```

5. **Run the FastAPI server**
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

## 📖 API Endpoints

### 1. Ingest Documents
**POST** `/ingest`

Processes all PDF files in `data/raw/` and builds the vector index.

```bash
curl -X POST http://localhost:8000/ingest
```

**Response**:
```json
{
  "status": "ingested",
  "files_processed": 5
}
```

### 2. Query Knowledge Base
**POST** `/query`

Query the ingested documents and get AI-generated answers.

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is John Doe'\''s education background?"}'
```

**Response**:
```json
{
  "query": "What is John Doe's education background?",
  "answer": "John Doe completed his Bachelor of Technology in Computer Science from NIT Durgapur...",
  "sources": ["Resume excerpt...", "Transcript excerpt..."]
}
```

## 💡 Sample Queries

- "What is John Doe's educational background?"
- "What are John Doe's professional skills and work experience?"
- "What are John Doe's recent blood test results?"
- "Where was John Doe born and raised?"
- "What are John Doe's hobbies and interests?"
- "Tell me about John Doe's gym routine."

##  Configuration

Edit `app/config.py` to customize:
- `DATA_PATH`: Path to raw documents
- `FAISS_INDEX_PATH`: Path to save vector index
- `EMBEDDING_MODEL`: Sentence Transformer model
- `LLM_MODEL`: Ollama model (default: Mistral)
- `TOP_K`: Number of documents to retrieve

##  How It Works

1. **Ingestion**: PDFs are loaded and split into chunks
2. **Embedding**: Each chunk is converted to a vector using Sentence Transformers
3. **Storage**: Vectors are stored in FAISS for fast similarity search
4. **Query**: User query is rewritten, documents are retrieved and reranked
5. **Generation**: Retrieved context is passed to Ollama (Mistral) for answer generation

##  Security

- `.env` file excluded from git (add API keys/secrets here)
- Local LLM (no cloud dependencies)
- Document data never leaves your machine

##  Logging

The application logs important events:
- Query processing steps
- Ollama API calls and responses
- Ingestion progress
- Errors and exceptions

Check terminal output for logs while using the API.

##  Deployment

### Local Development
Already running on `http://localhost:8000`

### Production
For production deployment:
1. Use a production ASGI server (Gunicorn + Uvicorn)
2. Configure environment variables in `.env`
3. Deploy on cloud platforms (AWS, GCP, Azure) or on-premises servers

##  Dependencies

See `requirements.txt` for full list. Key packages:
- `fastapi`: Web framework
- `sentence-transformers`: Embedding generation
- `faiss-cpu`: Vector search
- `pypdf`: PDF processing
- `torch`: Deep learning

##  Contributing

Feel free to fork and submit PRs for improvements!

##  License

MIT License - see LICENSE file for details

##  Author

Sahil Gupta - [GitHub](https://github.com/Sahil860860)

---

**Note**: This is a personal project demonstrating RAG principles and local AI integration. Customize it with your own documents to build your personal knowledge base!
