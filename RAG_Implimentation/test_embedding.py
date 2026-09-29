from openai import OpenAI
from similarity import cosine_similarity

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def create_embedding(content):
    embedding1 = client.embeddings.create(
    model="nomic-embed-text",
    input=content
    ).data[0].embedding
    return embedding1





