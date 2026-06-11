# AI Repository Assistant

## Features
- General AI Question Answering
- PDF Question Answering (RAG)
- GitHub Repository Question Answering
- LangGraph Intelligent Routing

## Tech Stack
- FastAPI
- Streamlit
- LangChain
- LangGraph
- ChromaDB
- HuggingFace Embeddings
- Groq

## Architecture

User Question
    ↓
LangGraph Router
    ↓
General AI | PDF RAG | Repo RAG
    ↓
Answer

## Screenshots

(Add screenshots here)

## How to Run

pip install -r requirements.txt

uvicorn backend.main:app --reload

streamlit run frontend/app.py
