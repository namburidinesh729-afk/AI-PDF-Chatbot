from utils.downloads import show_download_buttons
import streamlit as st
from pdf.pdf_processor import process_uploaded_pdf
from database.vector_store import (
    create_vector_store,
    load_vector_store
)
from core.chatbot import ask_groq
from core.summary import generate_summary
from core.quiz import generate_quiz
from core.notes import generate_notes
from core.flashcards import generate_flashcards
from core.interview import generate_interview_questions
from utils.export_pdf import create_pdf
from utils.export_docx import create_docx
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
    st.session_state.chat_history = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []    
if "db" not in st.session_state:
    st.session_state.db = None
if "summary" not in st.session_state:
    st.session_state.summary = None
if "quiz" not in st.session_state:
    st.session_state.quiz = None
if "notes" not in st.session_state:
    st.session_state.notes = None
if "flashcards" not in st.session_state:
    st.session_state.flashcards = None
if "interview" not in st.session_state:
    st.session_state.interview = None  
if "pdf_count" not in st.session_state:
    st.session_state.pdf_count = 0
if "last_uploaded_file" not in st.session_state:
    st.session_state.last_uploaded_file = ""      
# ------------------------------------
# Hero Banner
# ------------------------------------
st.markdown("""
<div style="
padding:30px;
border-radius:15px;
background:linear-gradient(90deg,#0f172a,#1e3a8a);
color:white;
text-align:center;
">
<h1>📚 AI Study Assistant</h1>
<h3>Powered by Groq • LangChain • FAISS</h3>
<p>
Chat with Multiple PDFs using AI
</p>
</div>
""", unsafe_allow_html=True)
st.markdown("### ✨ What can you do?")
feature1, feature2, feature3 = st.columns(3)
with feature1:
    st.info("""
📄 **Upload PDFs**
Process one or multiple PDF documents.
""")
with feature2:
    st.info("""
🤖 **Ask Questions**
Chat naturally with your documents.
""")
with feature3:
    st.info("""
🧠 **AI Study Tools**
Summary, Quiz, Notes, Flashcards & Interview Questions.
""")
st.markdown("## 📊 Dashboard")
dashboard_col1, dashboard_col2, dashboard_col3, dashboard_col4 = st.columns(4)
with dashboard_col1:
    if st.session_state.db:
        st.metric(
            "📚 PDFs",
            st.session_state.pdf_count
        )
    else:
        st.metric(
            "📚 PDFs",
            0
        )
with dashboard_col2:
    user_questions = sum(
        1
        for msg in st.session_state.messages
        if msg["role"] == "user"
    )
    st.metric("💬 Questions Asked", user_questions)
with dashboard_col3:
    st.metric(
        "🧠 Model",
        "Llama 3.3 70B"
    )
with dashboard_col4:
    st.metric(
        "⚡ Status",
        "Ready" if st.session_state.db else "Waiting"
    )    
st.markdown("### 🚀 Features")
feature_col1, feature_col2 = st.columns(2)
with feature_col1:
    st.success("💬 Ask Questions")
    st.success("📄 Generate Summary")
    st.success("❓ Generate Quiz")
    st.success("📝 Generate Notes")
with feature_col2:
    st.success("🧠 Generate Flashcards")
    st.success("🎯 Interview Questions")
    st.success("📚 Source References")
    st.success("⬇ Download Results")
# ------------------------------------
# Sidebar
# ------------------------------------
with st.sidebar:
    st.header("📂 Upload PDF")
    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )
    if uploaded_files:
        st.markdown("### 📄 Uploaded Files")
        for uploaded_file in uploaded_files:
            st.write(f"**📄 {uploaded_file.name}**")
            st.caption(
                f"Size: {round(uploaded_file.size/(1024*1024),2)} MB"
        )
        st.success(f"✅ {len(uploaded_files)} PDF(s) Ready for Processing")
        if st.button("Process PDF"):
            with st.spinner(
                "📄 Reading PDFs...\n\n"
                "🧠 Creating embeddings...\n\n"
                "⚡ Building AI knowledge base..."
            ):
                all_chunks = []
                for uploaded_file in uploaded_files:
                    chunks = process_uploaded_pdf(uploaded_file)
                    all_chunks.extend(chunks)
                create_vector_store(all_chunks)
                st.session_state.db = load_vector_store()
                st.session_state.pdf_count = len(uploaded_files)
                st.session_state.last_uploaded_file = ", ".join(
                    [pdf.name for pdf in uploaded_files]
                )
                st.session_state.summary = None
                st.session_state.quiz = None
                st.session_state.notes = None
                st.session_state.flashcards = None
                st.session_state.interview = None
            st.success(f"""
        ### ✅ Processing Complete
        📚 **{len(uploaded_files)} PDF(s) processed successfully!**
        Your AI Study Assistant is ready.
        You can now:
        • 💬 Chat with your PDFs
        • 📄 Generate Summary
        • ❓ Generate Quiz
        • 📝 Generate Notes
        • 🧠 Generate Flashcards
        • 🎯 Interview Questions
        """)
            st.balloons()
    st.divider()
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.subheader("⚙️ System Information")
    st.info("🧠 Embedding\n\nall-MiniLM-L6-v2")
    st.info("🗂️ Vector Database\n\nFAISS")
    st.info("🤖 AI Model\n\nLlama 3.3 70B")
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
        with st.spinner("📄 Generating Summary..."):
            try:
                st.session_state.summary = generate_summary(context)
            except Exception as e:
                st.error(
                    f"❌ {e}"
                )
                st.stop()
    
    # ---------------- Quiz ----------------
    if quiz_btn:
        with st.spinner("Generating Quiz..."):
            try:
                st.session_state.quiz = generate_quiz(context)
            except Exception as e:
                st.error(
                    f"❌ {e}"
                )
                st.stop()
      
    # ---------------- Notes ----------------
    if notes_btn:
        with st.spinner("Generating Notes..."):
            try:
                st.session_state.notes = generate_notes(context)
            except Exception as e:
                st.error(
                    f"❌ {e}"
                )
                st.stop()
       
    # ---------------- Flashcards ----------------
    if flashcards_btn:
        with st.spinner("Generating Flashcards..."):
            try:
                st.session_state.flashcards = generate_flashcards(context)
            except Exception as e:
                st.error(
                    f"❌ {e}"
                )
                st.stop()
   
    # ---------------- Interview ----------------
    if interview_btn:
        with st.spinner("Generating Interview Questions..."):
            try:
                st.session_state.interview = generate_interview_questions(context)
            except Exception as e:
                st.error(
                    f"❌ {e}"
                )
                st.stop()
st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📄 Summary",
    "❓ Quiz",
    "📝 Notes",
    "🧠 Flashcards",
    "🎯 Interview"
])

with tab1:
    if st.session_state.summary:
        st.write(st.session_state.summary)
        show_download_buttons(
            st.session_state.summary,
            "summary"
        )
    else:
        st.info(
            "📄 Generate a summary from the sidebar to view it here."
        )

with tab2:
    if st.session_state.quiz:
        st.write(st.session_state.quiz)
        show_download_buttons(
            st.session_state.quiz,
            "quiz"
        )
    else:
        st.info(
            "❓ Generate a quiz from the sidebar to view it here."
        )

with tab3:
    if st.session_state.notes:
        st.write(st.session_state.notes)
        show_download_buttons(
            st.session_state.notes,
            "notes"
        )
    else:
        st.info(
            "📝 Generate notes from the sidebar to view them here."
        )

with tab4:
    if st.session_state.flashcards:
        st.write(st.session_state.flashcards)
        show_download_buttons(
            st.session_state.flashcards,
            "flashcards"
        )
    else:
        st.info(
            "🧠 Generate flashcards from the sidebar to view them here."
        )

with tab5:
    if st.session_state.interview:
        st.write(st.session_state.interview)
        show_download_buttons(
            st.session_state.interview,
            "interview_questions"
        )
    else:
        st.info(
            "🎯 Generate interview questions from the sidebar to view them here."
        ) 
    # ------------------------------------
# Chat with PDF
# ------------------------------------
if st.session_state.db is not None:
    st.divider()
    st.header("🤖 AI Tutor")
    st.caption(
        "Ask questions naturally. The AI will answer using information from your uploaded documents."
    )
    question = st.chat_input(
        "💬 Ask any question about your uploaded documents..."
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
                history = "\n".join(st.session_state.chat_history)
                answer = ask_groq(
                    context,
                    question,
                    history
                )
            except Exception as e:
                st.error(
                    f"❌ Groq Error:\n\n{e}"
                )
                st.stop()
        sources = []
        for doc in docs:
            source = doc.metadata.get("source", "Unknown PDF")
            page = doc.metadata.get("page", "Unknown")
            item = f"📄 {source} — Page {page}"
            if item not in sources:
                sources.append(item)
        answer += "\n\n---"
        answer += "\n### 📚 Sources\n"
        for item in sources:
            answer += f"\n• {item}"
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
        st.session_state.chat_history.append(
            f"User: {question}"
        )
        st.session_state.chat_history.append(
            f"Assistant: {answer}"
        )
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])    
st.divider()
st.caption(
    "🚀 Built by Dinesh Namburi | Powered by Streamlit • LangChain • FAISS • Hugging Face • Groq (Llama 3.3 70B Versatile)"
)