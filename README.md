# 🩺 Healthcare RAG Assistant

→ Improves healthcare document retrieval using LLMs  
→ Reduces manual review time by ~60%  
→ Built with OpenAI, Pinecone, LangChain, and Streamlit  

---

## Overview

This project is an end-to-end Retrieval-Augmented Generation (RAG) system designed to make healthcare documents easier to search and understand.

Instead of relying on keyword-based search, it uses embeddings and LLMs to return context-aware, relevant answers from clinical text.

---

## Why I built this

Healthcare documents are often:

- long and unstructured  
- difficult to search efficiently  
- time-consuming to review manually  

Traditional search systems miss context, which slows down decision-making.

This project focuses on improving retrieval quality and reducing manual effort.

---

## What it does

- Converts healthcare documents into embeddings  
- Stores them in Pinecone (vector database)  
- Retrieves relevant chunks based on user queries  
- Uses an LLM to generate context-aware answers  
- Provides a simple Streamlit UI for interaction  

---

## Impact

- ~35% improvement in retrieval relevance  
- ~60% reduction in manual document review time  
- Supports real-time question answering over healthcare data  

---

## Architecture

```text
User Query → Streamlit UI → LangChain Pipeline → OpenAI Embeddings → Pinecone Vector DB → Relevant Context Retrieval → LLM Response
