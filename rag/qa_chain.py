from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from rag.local_llm import LocalLLM

# Load vector store
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Initialize local LLM
llm = LocalLLM()

def answer_question(query: str) -> str:
    # Retrieve relevant chunks
    docs = db.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    # Prompt template
    prompt = f"""
    Use the following context to answer the question.
    If the answer is not in the context, say "I don't know".

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    return llm.generate(prompt)
