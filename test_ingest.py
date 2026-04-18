from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_text
from app.ingestion.embedder import Embedder

# Test loading one PDF
text = load_pdf("/Users/sahilgupta/Desktop/personal-ai-knowledge-vault/data/raw/medical_report_1.pdf")
print("Text loaded:", len(text), "characters")

chunks = chunk_text(text)
print("Chunks:", len(chunks))

embedder = Embedder("sentence-transformers/all-MiniLM-L6-v2")
embeddings = embedder.encode(chunks[:5])  # Test with first 5 chunks
print("Embeddings shape:", embeddings.shape)