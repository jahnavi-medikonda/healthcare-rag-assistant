# Healthcare RAG Assistant

End-to-end Retrieval-Augmented Generation (RAG) system using OpenAI embeddings, Pinecone vector database, and Streamlit UI for querying healthcare documents.

---

## 🚀 Features
- Semantic search using OpenAI embeddings  
- Vector search using Pinecone  
- Context-aware answer generation using GPT  
- Streamlit UI for real-time querying  

---

## 💡 Problem

Healthcare data is often stored in large, unstructured documents such as clinical notes, reports, and patient records. Traditional keyword-based search lacks semantic understanding, making it difficult to retrieve accurate and relevant information.

This leads to:
- Time-consuming manual document review  
- Incomplete or irrelevant search results  
- Slower decision-making workflows  

---

## 🧠 Solution

This project implements a Retrieval-Augmented Generation (RAG) system to enable intelligent document search and question answering over healthcare data.

---

## ⚙️ Approach

1. Preprocessed and cleaned clinical documents  
2. Chunked documents into meaningful segments  
3. Generated embeddings using OpenAI  
4. Stored vectors in Pinecone  
5. Retrieved top-k relevant context using similarity search  
6. Generated responses using GPT based on retrieved context  

---

## 📊 Impact
- Improved retrieval relevance using semantic search  
- Reduced manual document lookup effort  
- Enabled real-time querying of healthcare data  

---

## 🖥️ Demo

![UI](screenshots/ui.png)

---

## ⚙️ Tech Stack
- Python  
- OpenAI API  
- Pinecone  
- Streamlit  
- AWS  

---

## ▶️ Run Locally

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m streamlit run streamlit_app/app.py
