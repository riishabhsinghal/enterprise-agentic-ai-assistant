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
# Main Interface
# -------------------------------
st.title("Enterprise AI Assistant")
st.markdown("Chat with the assistant below. It can answer HR & math queries.")

# -------------------------------
# Chat History in Session
# -------------------------------
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display previous messages
for message in st.session_state['chat_history']:
    role = "user" if message['role'] == 'user' else 'assistant'
    st.chat_message(role).write(message['message'])

# -------------------------------
# Chat Input
# -------------------------------
user_input = st.chat_input("Ask a question...")

if user_input:
    # Save user message
    st.session_state.chat_history.append({"role": "user", "message": user_input})

    # Get agent response
    try:
        response = route_query(user_input)
    except Exception:
        response = "⚠️ Sorry, something went wrong. Please try again."

    # Save & display assistant message
    st.session_state.chat_history.append({"role": "assistant", "message": response})
    st.chat_message("assistant").write(response)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("*This is a demo application. Enterprise deployment would require authentication and monitoring.*")
