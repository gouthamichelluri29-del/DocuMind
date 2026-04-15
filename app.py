'''
this app will do :
- upload pdf
- read and split document
- create embeddings
- store in FAISS
- ask question 
- retrive relevant chunks
- send context to LLM
- show answer and source chunks
'''
import os 
import tempfile
from pathlib import Path
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

#app page title:

st.set_page_config(page_title="DocuMind", layout = "wide")

st.title("DocuMind - Enterprise Document Q&A system")
st.write("Upload a PDF, ask questionns, and get the answers grounded in the document.")

#load embedding and LLM

@st.cache_resource #does not reload the model every time the page refreshes.

def load_embedding():
    return HuggingFaceEmbeddings(
        model_name = 'sentence-transformers/all-MiniLM-L6-v2'
    )

@st.cache_resource

def load_llm():
    return Ollama(model = 'llama3')

embedding_model = load_embedding()
llm = load_llm()

#document processing function - reads, splits and stores chunks in FAISS

def process_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete= False, suffix= ".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_file_path = tmp_file.name #reads
    loader = PyPDFLoader(temp_file_path)
    docs= loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap = 20
    )

    split_docs = text_splitter.split_documents(docs) #splits

    vectorstore = FAISS.from_documents(split_docs, embedding_model) #stores

    return vectorstore, split_docs

#RAG Function

def rag(query, vectorstore, llm):
    retriever = vectorstore.as_retriever(search_kwargs={'k':3})
    docs= retriever.invoke(query)

    context = '\n\n'.join([doc.page_content for doc in docs])

    prompt = f""" 
    Answer the question using ONLY the context below.

    Context: 
    {context}

    Question:
    {query}

    Answer:
    """
    response = llm.invoke(prompt)
    return response, docs

#user to upload file

uploaded_file = st.file_uploader("Upload a PDF document", type=['pdf'])

#store the doc

if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None

if 'split_docs' not in st.session_state:
    st.session_state.split_docs = None


#upload file in session state

if uploaded_file is not None:
    with st.spinner("Processing document..."):
        vectorstore, split_docs = process_pdf(uploaded_file)
        st.session_state.vectorstore = vectorstore
        st.session_state.split_docs = split_docs

    st.success('Document processed successfully')
    st.write(f"Total chunks created: {len(split_docs)}")

query = st.text_input("Ask a question about the document")

#generating answer

if st.session_state.vectorstore is not None and query:
    with st.spinner("Generating answer..."):
        answer, source_docs = rag(query, st.session_state.vectorstore, llm)

    st.subheader('Answer')
    st.write(answer)

    st.subheader('Source chunks')
    for i, doc in enumerate(source_docs, 1):
        with st.expander(f"Source Chunk {i}"):
            st.write(doc.page_content)
            st.write("Metadata:",doc.metadata)
