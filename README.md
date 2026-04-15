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

## Tech Stack

- **LangChain** — pipeline orchestration  
- **FAISS** — vector database for semantic search  
- **HuggingFace Embeddings** — text vectorization  
- **LLaMA (Ollama)** — local LLM  
- **Streamlit** — web interface  
- **MLflow (optional)** — experiment tracking  

---

