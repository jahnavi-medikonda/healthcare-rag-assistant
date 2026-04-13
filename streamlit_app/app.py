import os
import sys
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Allow imports from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.query_rag import query_rag

load_dotenv()

st.set_page_config(page_title="Healthcare RAG Assistant", layout="wide")
st.title("Healthcare RAG Assistant")
st.write("Ask questions over the healthcare notes indexed in Pinecone.")

question = st.text_input("Ask a question:")

if st.button("Search"):
    if question.strip():
        with st.spinner("Searching and generating answer..."):
            answer = query_rag(question)

        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")
