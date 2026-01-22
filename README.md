# Enterprise Agentic AI Assistant

An enterprise-focused Agentic AI Assistant built using Retrieval-Augmented Generation (RAG), FAISS, and local LLMs, with a Streamlit-based chat interface.

## 🚀 Features
- Agent-based query routing (HR & Math agents)
- Retrieval-Augmented Generation (RAG) for enterprise documents
- Local embeddings and LLM (no OpenAI API required)
- Streamlit chat UI for interactive usage
- Zero external API cost

## 🧠 Architecture
- **HR Agent** → RAG over company documents
- **Math Agent** → Tool-based arithmetic computation
- **Router Agent** → Intent-based query routing

## 🛠 Tech Stack
- Python
- LangChain
- FAISS
- HuggingFace embeddings
- Streamlit

## ▶️ How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
