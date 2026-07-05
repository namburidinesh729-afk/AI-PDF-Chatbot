
import streamlit as st
from pdf.pdf_processor import process_uploaded_pdf
from database.vector_store import load_vector_store
from core.chatbot import ask_groq
from core.summary import generate_summary
from core.quiz import generate_quiz
from core.notes import generate_notes
from core.flashcards import generate_flashcards
from core.interview import generate_interview_questions
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)
# ------------------------------------
# Session State
# ------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "db" not in st.session_state:
    st.session_state.db = None
    # ------------------------------------
# Title
# ------------------------------------
st.title("📚 AI Study Assistant")
st.markdown("""
## Learn Smarter with AI 🤖
Upload your PDF and let AI become your personal tutor.
""")
st.markdown("### 🚀 Features")
col1, col2 = st.columns(2)
with col1:
    st.success("💬 Ask Questions")
    st.success("📄 Generate Summary")
    st.success("❓ Generate Quiz")
    st.success("📝 Generate Notes")
    
with col2:
    st.success("🧠 Generate Flashcards")
    st.success("🎯 Interview Questions")
    st.success("📚 Source References")
    st.success("⬇ Download Results")
# ------------------------------------
# Sidebar
# ------------------------------------
with st.sidebar:
    st.header("📂 Upload PDF")
    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )
    if uploaded_file:
        if st.button("Process PDF"):
            with st.spinner("Processing PDF..."):
                process_uploaded_pdf(uploaded_file)
            st.session_state.db = load_vector_store()
            st.success(f"✅ {uploaded_file.name} processed successfully!")
    st.divider()
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.subheader("Project Information")
    st.write("Embedding Model")
    st.caption("all-MiniLM-L6-v2")
    st.write("Vector Database")
    st.caption("FAISS")
    st.write("LLM")
    st.caption("Groq (Llama 3.3 70B Versatile)")
    st.divider()
    st.subheader("📚 AI Features")
    summary_btn = st.button("📄 Generate Summary")
    quiz_btn = st.button("❓ Generate Quiz")
    notes_btn = st.button("📝 Generate Notes")
    flashcards_btn = st.button("🧠 Generate Flashcards")
    interview_btn = st.button("🎯 Interview Questions")
if st.session_state.db is None:
    st.info("👈 Upload a PDF from the sidebar and click 'Process PDF' to begin.")
    # ------------------------------------
# AI Features
# ------------------------------------
if st.session_state.db is not None:
    docs = st.session_state.db.similarity_search(
        "entire document",
        k=10
    )
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )
    # ---------------- Summary ----------------
    if summary_btn:
        with st.spinner("Generating Summary..."):
            try:
                summary = generate_summary(context)
            except Exception as e:
                st.error(
                    f"❌ {e}"
                )
                st.stop()
        st.subheader("📄 Summary")
        st.write(summary)
        st.download_button(
            label="⬇ Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )
    # ---------------- Quiz ----------------
    if quiz_btn:
        with st.spinner("Generating Quiz..."):
            try:
                quiz = generate_quiz(context)
            except Exception as e:
                st.error(
                    f"❌ {e}"
                )
                st.stop()
        st.subheader("❓ Quiz")
        st.write(quiz)
        st.download_button(
            label="⬇ Download Quiz",
            data=quiz,
            file_name="quiz.txt",
            mime="text/plain"
        )
    # ---------------- Notes ----------------
    if notes_btn:
        with st.spinner("Generating Notes..."):
            try:
                notes = generate_notes(context)
            except Exception as e:
                st.error(
                    f"❌ {e}"
                )
                st.stop()
        st.subheader("📝 Notes")
        st.write(notes)
        st.download_button(
            label="⬇ Download Notes",
            data=notes,
            file_name="notes.txt",
            mime="text/plain"
        )
    # ---------------- Flashcards ----------------
    if flashcards_btn:
        with st.spinner("Generating Flashcards..."):
            try:
                flashcards = generate_flashcards(context)
            except Exception as e:
                st.error(
                    f"❌ {e}"
                )
                st.stop()
        st.subheader("🧠 Flashcards")
        st.write(flashcards)
        st.download_button(
            label="⬇ Download Flashcards",
            data=flashcards,
            file_name="flashcards.txt",
            mime="text/plain"
        )
    # ---------------- Interview ----------------
    if interview_btn:
        with st.spinner("Generating Interview Questions..."):
            try:
                interview = generate_interview_questions(context)
            except Exception as e:
                st.error(
                    f"❌ {e}"
                )
                st.stop()
        st.subheader("🎯 Interview Questions")
        st.write(interview)
        st.download_button(
            label="⬇ Download Interview Questions",
            data=interview,
            file_name="interview_questions.txt",
            mime="text/plain"
        )       
    # ------------------------------------
# Chat with PDF
# ------------------------------------
if st.session_state.db is not None:
    st.divider()
    st.subheader("💬 Chat with your PDF")
    question = st.chat_input(
        "Ask anything about your PDF..."
    )
    if question:
        # Store User Message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )
        docs = st.session_state.db.max_marginal_relevance_search(
            question,
            k=5,
            fetch_k=15
        )
        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )
        with st.spinner("🤖 AI is thinking..."):
            try:
                answer = ask_groq(
                    context,
                    question
                )
            except Exception as e:
                st.error(
                    f"❌ Groq Error:\n\n{e}"
                )
                st.stop()
        pages = sorted(
            {
                doc.metadata.get("page", "Unknown")
                for doc in docs
            }
        )
        answer += "\n\n📄 **Sources**\n"
        for page in pages:
            answer += f"\n• Page {page}"
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])    
st.divider()
st.caption(
    "🚀 Built by Dinesh Namburi | Powered by Streamlit • LangChain • FAISS • Hugging Face • Groq (Llama 3.3 70B Versatile)"
)