import requests
import logging

logger = logging.getLogger(__name__)

def generate_answer(query, context):
    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {query}
    """

    logger.info(f"Sending query to Ollama: {query[:100]}...")
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt, "stream": False}
        )
        response.raise_for_status()
        result = response.json()["response"]
        logger.info(f"Received response from Ollama: {result[:100]}...")
        return result
    except requests.RequestException as e:
        logger.error(f"Error calling Ollama: {e}")
        return "Error: Unable to generate answer from LLM."
