import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check .env file")

print("API key loaded:", api_key[:10])  # debug

client = OpenAI(api_key=api_key)

try:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input="Patient has diabetes"
    )

    embedding = response.data[0].embedding

    print("✅ SUCCESS")
    print("Embedding length:", len(embedding))
    print("First 5 values:", embedding[:5])

except Exception as e:
    print("❌ ERROR:")
    print(e)
