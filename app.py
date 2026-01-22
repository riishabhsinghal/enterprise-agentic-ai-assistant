import streamlit as st
# Sidebar information
st.sidebar.markdown("""
### 🧠 Enterprise AI Assistant
Ask HR-related questions or math queries.

⚠️ Demo application  
📄 Knowledge limited to uploaded documents
""")
from agents.router import route_query

st.set_page_config(page_title="Enterprise AI Assistant", layout="centered")

st.title("🏢 Enterprise AI Assistant")
st.caption("Agentic AI powered by RAG & Local LLM")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_query = st.chat_input("Ask a question...")

if user_query:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )
    with st.chat_message("user"):
        st.markdown(user_query)

    # Agent response
    response = route_query(user_query)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.markdown(response)
