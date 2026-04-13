import os
import json
import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter

INPUT_PATH = "data/processed/cleaned_docs.csv"
OUTPUT_PATH = "data/processed/chunked_docs.json"


def main():
    os.makedirs("data/processed", exist_ok=True)

    df = pd.read_csv(INPUT_PATH)

    print("Loaded cleaned data:", df.shape)
    print("Columns:", df.columns.tolist())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=75
    )

    chunked_docs = []

    for i, row in df.iterrows():
        text = str(row["text"]).strip()
        if not text:
            continue

        chunks = splitter.split_text(text)

        for j, chunk in enumerate(chunks):
            chunked_docs.append({
                "id": f"doc_{i}_chunk_{j}",
                "text": chunk,
                "metadata": {
                    "title": str(row.get("title", "")),
                    "specialty": str(row.get("specialty", "")),
                    "keywords": str(row.get("keywords", ""))
                }
            })

    with open(OUTPUT_PATH, "w") as f:
        json.dump(chunked_docs, f, indent=2)

    print("Total chunks created:", len(chunked_docs))
    print(f"Saved chunked file to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
