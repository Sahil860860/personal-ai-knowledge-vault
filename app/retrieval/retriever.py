class Retriever:
    def __init__(self, vector_store, embedder):
        self.vector_store = vector_store
        self.embedder = embedder

    def retrieve(self, query, k=5):
        query_embedding = self.embedder.encode([query])
        return self.vector_store.search(query_embedding, k)
