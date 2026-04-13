import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

INPUT_PATH = "data/processed/chunked_docs.json"

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX_NAME", "healthcare-rag-index")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found")

if not pinecone_api_key:
    raise ValueError("PINECONE_API_KEY not found")

client = OpenAI(api_key=openai_api_key)
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index(index_name)

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

with open(INPUT_PATH, "r") as f:
    docs = json.load(f)

print("Loaded docs:", len(docs))

batch = []
batch_size = 20

for i, doc in enumerate(docs):
    embedding = get_embedding(doc["text"])

    batch.append({
        "id": doc["id"],
        "values": embedding,
        "metadata": {
   		 "text": doc["text"],   # 👈 THIS IS THE KEY FIX
   		 "title": doc["metadata"].get("title", ""),
   		 "specialty": doc["metadata"].get("specialty", "")
}
    })

    if len(batch) == batch_size:
        index.upsert(vectors=batch)
        print("Upserted:", i)
        batch = []

if batch:
    index.upsert(vectors=batch)

print("Done")
