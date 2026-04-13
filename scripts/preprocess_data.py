import os
import pandas as pd

INPUT_PATH = "data/raw/Healthcare Documentation Database.csv"
OUTPUT_PATH = "data/processed/cleaned_docs.csv"

def main():
    os.makedirs("data/processed", exist_ok=True)

    df = pd.read_csv(INPUT_PATH)

    print("Original shape:", df.shape)
    print("Columns:", df.columns.tolist())

    required_cols = [
        "cleaned_transcription",
        "medical_specialty",
        "sample_name",
        "keywords",
    ]

    df = df[required_cols].copy()

    df = df.dropna(subset=["cleaned_transcription", "medical_specialty", "sample_name"])

    df = df.rename(columns={
        "cleaned_transcription": "text",
        "medical_specialty": "specialty",
        "sample_name": "title",
    })

    df["text"] = df["text"].astype(str).str.strip()
    df = df[df["text"].str.len() > 300]

    # Do NOT filter specialties for now
    # df = df[df["specialty"].isin(selected_specialties)]

    df = df.head(200).reset_index(drop=True)

    print("Cleaned shape:", df.shape)
    print(df["specialty"].value_counts().head(10))

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved cleaned file to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
