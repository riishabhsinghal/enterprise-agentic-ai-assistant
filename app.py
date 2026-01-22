# app.py
import streamlit as st
from agents.router import route_query
# Sidebar
# -------------------------------
st.sidebar.title("🤖 Enterprise AI Assistant")
st.sidebar.markdown("""
Ask HR questions or math queries.  
The system intelligently routes your query to the correct agent.

⚠️ Demo only: Knowledge limited to uploaded company documents.
""")

# Optional: Add GitHub & live demo links
st.sidebar.markdown("---")
st.sidebar.markdown(
    "📂 [GitHub Repo](https://github.com/RiishabhSinghal/enterprise-agentic-ai-assistant)  \n"
    "🌐 [Live Demo](https://enterprise-agentic-ai-assistant-egkzezxeyev7obbfxqmc7o.streamlit.app)"
)

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

import streamlit as st
from agents.router import route_query  # Your agent routing logic

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Enterprise AI Assistant",
    page_icon="🤖",
    layout="centered"
)
# Main Interface
# -------------------------------
st.title("Enterprise AI Assistant")
st.markdown("Chat with the assistant below. It can answer HR & math queries.")
# Footer
# -------------------------------
st.markdown("---")
st.markdown("*This is a demo application. Enterprise deployment would require authentication and monitoring.*")
