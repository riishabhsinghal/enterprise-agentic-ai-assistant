# app.py

# -------------------------------
# Imports
# -------------------------------
import streamlit as st
from agents.router import route_query  # Your agent routing logic

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="Enterprise AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🤖 Enterprise AI Assistant")
st.sidebar.markdown(
"""
Welcome to the Enterprise AI Assistant demo.  

### ⚡ Features
- Ask HR-related questions (policies, leave, etc.)
- Ask Math/Calculation queries
- Agentic AI routing (HR / Math / Default)

**⚠️ Note:** Knowledge limited to uploaded company documents.
"""
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "📂 **Project repo:** [GitHub](https://github.com/RiishabhSInghal/enterprise-agentic-ai-assistant)  \n"
    "🌐 **Live Demo:** [Streamlit Cloud](https://enterprise-agentic-ai-assistant-egkzezxeyev7obbfxqmc7o.streamlit.app)"
)

# -------------------------------
# Main Page
# -------------------------------
st.title("Enterprise AI Assistant")
st.markdown(
"""
Welcome! Ask questions related to HR policies or perform quick calculations.  
The system intelligently routes your query to the correct agent.
"""
)

# Optional: Add instructions for users
st.info("Type a question below and press Enter or click 'Send'.")

# -------------------------------
# Chat Input & Agent Response
# -------------------------------
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display chat history
for entry in st.session_state.chat_history:
    if entry['role'] == 'user':
        st.chat_message("user").write(entry['message'])
    else:
        st.chat_message("assistant").write(entry['message'])

# Chat input
user_query = st.chat_input("Ask a question...")

if user_query:
    # Save user query
    st.session_state.chat_history.append({"role": "user", "message": user_query})

    # Get response from routing agent
    try:
        response = route_query(user_query)
    except Exception as e:
        response = "⚠️ Sorry, something went wrong. Please try again."

    # Save and display response
    st.session_state.chat_history.append({"role": "assistant", "message": response})
    st.chat_message("assistant").write(response)

# -------------------------------
# Footer / Notes
# -------------------------------
st.markdown("---")
st.markdown(
"""
*This is a demo application. For enterprise deployment, authentication, monitoring, and additional security would be required.*
"""
)
