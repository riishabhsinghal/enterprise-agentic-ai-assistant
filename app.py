# app.py

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

# -------------------------------
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

# -------------------------------
# Main Page
# -------------------------------
st.title("🏢 Enterprise AI Assistant")
st.caption("Agentic AI powered by RAG & Local LLM")
st.markdown("Chat with the assistant below. It can answer HR & math queries.")

# -------------------------------
# Initialize Chat History
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------
# User Input
# -------------------------------
user_query = st.chat_input("Ask a question...")

if user_query:
    # Save and display user message
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Get agent response
    try:
        response = route_query(user_query)
    except Exception:
        response = "⚠️ Sorry, something went wrong. Please try again."

    # Save and display assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

# -------------------------------
# Footer / Notes
# -------------------------------
st.markdown("---")
st.markdown("*This is a demo application. Enterprise deployment would require authentication and monitoring.*")
