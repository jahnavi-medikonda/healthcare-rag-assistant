import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX_NAME")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

if not pinecone_api_key:
    raise ValueError("PINECONE_API_KEY not found in .env")

if not index_name:
    raise ValueError("PINECONE_INDEX_NAME not found in .env")

client = OpenAI(api_key=openai_api_key)
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index(index_name)


def get_embedding(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


def query_rag(question: str):
    query_vector = get_embedding(question)

    results = index.query(
        vector=query_vector,
        top_k=3,
        include_metadata=True
    )

    contexts = []

    for match in results.matches:
        metadata = match.metadata or {}
        text = metadata.get("text", "")
        if text:
            contexts.append(text)

    if not contexts:
        return "No relevant context found in Pinecone."

    context_text = "\n\n".join(contexts)

    prompt = f"""
You are answering from retrieved healthcare note context.

Use only the context below.
If the context does not clearly contain the answer, say:
"The retrieved notes do not clearly mention that."

Context:
{context_text}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    question = "What medical conditions are mentioned in the retrieved notes?"
    answer = query_rag(question)

    print("\nQUESTION:", question)
    print("\nANSWER:", answer)
