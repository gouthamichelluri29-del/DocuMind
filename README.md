# DocuMind - Enterprise Document Intelligence System

DocuMind is a Retrieval-Augmented Generation (RAG) based system that allows users to upload documents and ask natural language questions. The system retrieves relevant content from the document and generates accurate, context-aware answers using a Large Language Model (LLM).

---

## Features

- Upload PDF documents
- Semantic search using FAISS vector database
- Context-aware answer generation using LLM (LLaMA via Ollama)
- Prompt engineering (basic, chain-of-thought, few-shot)
- Optional) MLflow tracking for prompt evaluation
- Source chunk display for transparency and reduced hallucination
- Interactive UI using Streamlit

---

## How It Works

DocuMind follows a **Retrieval-Augmented Generation (RAG)** pipeline:

1. Document Upload  
2. Text Chunking  
3. Embedding Generation  
4. Vector Storage (FAISS)  
5. Retrieval of Relevant Chunks  
6. Prompt Construction  
7. LLM Answer Generation  
8. Display Answer + Source Chunks  

---
## Data

This project does not include sample datasets.

You can test the system using your own PDF documents by uploading them through the application interface.

--- 

## Tech Stack

- **LangChain** — pipeline orchestration  
- **FAISS** — vector database for semantic search  
- **HuggingFace Embeddings** — text vectorization  
- **LLaMA (Ollama)** — local LLM  
- **Streamlit** — web interface  
- **MLflow (optional)** — experiment tracking  

## Installation

Clone the repository
pip install -r requirements.txt
- Setup LLM (Ollama) : ollama run llama3
- Run the App : streamlit run app.py

## Working app model:
You can upload the pdf document and ask questions in here 😊 : https://gouthamichelluri29-del-documind-documind-grok-ai29t6.streamlit.app/
