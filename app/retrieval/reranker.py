def rerank(query, docs):
    # Simple heuristic (replace with cross-encoder later)
    return sorted(docs, key=lambda x: len(x), reverse=True)
