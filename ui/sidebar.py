import streamlit as st
def show_sidebar():
    with st.sidebar:
        st.title("📚 AI Study Assistant")
        uploaded_file = st.file_uploader(
            "Upload PDF",
            type=["pdf"]
        )
        clear_chat = st.button("🧹 Clear Chat")
        st.divider()
        st.subheader("ℹ️ Project Information")
        st.write("Embedding Model")
        st.caption("all-MiniLM-L6-v2")
        st.write("Vector Store")
        st.caption("FAISS")
        st.write("LLM")
        st.caption("Gemini 2.5 Flash")
    return uploaded_file, clear_chat