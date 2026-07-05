# from utils import read_pdf
# pdf_path = "pdfs/notes.pdf"
# text = read_pdf(pdf_path)
# print(text[:1000])


# from utils import read_pdf
# from text_splitter import split_text
# pdf_path = "pdfs/notes.pdf"
# text = read_pdf(pdf_path)
# chunks = split_text(text)
# print(f"Total Chunks: {len(chunks)}")
# print("\nFirst Chunk:\n")
# print(chunks[0])

# from utils import read_pdf
# from text_splitter import split_text
# from vector_store import create_vector_store
# pdf_path = "pdfs/notes.pdf"
# text = read_pdf(pdf_path)
# chunks = split_text(text)
# print(f"Total Chunks: {len(chunks)}")
# create_vector_store(chunks)
# print("Vector Store Created Successfully!")

# from vector_store import load_vector_store
# db = load_vector_store()
# query = input("Ask your question: ")
# docs = db.similarity_search(query, k=3)
# print("\nTop 3 Relevant Chunks\n")
# for i, doc in enumerate(docs, start=1):
#     print("=" * 60)
#     print(f"Chunk {i}\n")
#     print(doc.page_content)
#     print()


# from vector_store import load_vector_store
# from chatbot import ask_gemini
# db = load_vector_store()
# while True:
#     question = input("\nAsk a question (type 'exit' to quit): ")
#     if question.lower() == "exit":
#         break
#     docs = db.similarity_search(question, k=3)
#     context = "\n\n".join(
#         doc.page_content
#         for doc in docs
#     )
#     answer = ask_gemini(context, question)
#     print("\nAnswer:\n")
#     print(answer)


# from vector_store import load_vector_store
# from chatbot import ask_gemini
# db = load_vector_store()
# print("📄 AI PDF Chatbot")
# print("Type 'exit' to quit.\n")
# while True:
#     question = input("You: ")
#     if question.lower() == "exit":
#         print("Goodbye!")
#         break
#     docs = db.similarity_search(question, k=3)
#     context = "\n\n".join(
#         doc.page_content
#         for doc in docs
#     )
#     answer = ask_gemini(context, question)
#     print("\n🤖 AI:\n")
#     print(answer)
#     print("\n" + "-" * 60 + "\n")

# import streamlit as st 
# from vector_store import load_vector_store
# from chatbot import ask_gemini
# st.set_page_config(
#     page_title="AI PDF Chatbot",
#     page_icon="📄"
# )
# st.title("📄 AI PDF Chatbot")
# db = load_vector_store()
# question = st.text_input("Ask a question about your PDF")
# if st.button("Ask"):
#     docs = db.similarity_search(question, k=3)
#     context = "\n\n".join(
#         doc.page_content
#         for doc in docs
#     )
#     answer = ask_gemini(context, question)
#     st.subheader("Answer")
#     st.write(answer)


# import streamlit as st
# from vector_store import load_vector_store
# from chatbot import ask_gemini
# st.set_page_config(
#     page_title="AI PDF Chatbot",
#     page_icon="📄",
#     layout="wide"
# )
# st.title("📄 AI PDF Chatbot")
# db = load_vector_store()
# question = st.text_input("Ask a question about your PDF")
# if st.button("Ask"):
#     if question.strip() == "":
#         st.warning("Please enter a question.")
#     else:
#         docs = db.similarity_search(question, k=3)
#         context = "\n\n".join(
#             doc.page_content for doc in docs
#         )
#         with st.spinner("🤖 Gemini is thinking..."):
#             answer = ask_gemini(context, question)
#         st.subheader("Answer")
#         st.write(answer)

# import streamlit as st

# from pdf_processor import process_uploaded_pdf
# from vector_store import load_vector_store
# from chatbot import ask_gemini

# st.set_page_config(
#     page_title="AI PDF Chatbot",
#     page_icon="📄",
#     layout="wide"
# )

# st.title("📄 AI PDF Chatbot")
# uploaded_file = st.file_uploader(
#     "Upload a PDF",
#     type=["pdf"]
# )
# if uploaded_file:
#     if st.button("Process PDF"):
#         with st.spinner("Processing PDF..."):
#             process_uploaded_pdf(uploaded_file)
#         st.success("PDF processed successfully!")
# if st.button("Load PDF"):
#     st.session_state.db = load_vector_store()
# if "db" in st.session_state:
#     question = st.text_input("Ask a question")
#     if st.button("Ask"):
#         docs = st.session_state.db.similarity_search(
#             question,
#             k=5
#         )
#         context = "\n\n".join(
#             doc.page_content for doc in docs
#         )
#         with st.spinner("Gemini is thinking..."):
#             answer = ask_gemini(context, question)
#         st.subheader("Answer")
#         st.write(answer)

# import streamlit as st
# from pdf_processor import process_uploaded_pdf
# from vector_store import load_vector_store
# from chatbot import ask_gemini
# st.set_page_config(
#     page_title="AI PDF Chatbot",
#     page_icon="📄",
#     layout="wide"
# )
# st.title("📄 AI PDF Chatbot")
# # -----------------------------
# # Chat History Initialization
# # -----------------------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# # -----------------------------
# # PDF Upload Section
# # -----------------------------
# uploaded_file = st.file_uploader(
#     "Upload a PDF",
#     type=["pdf"]
# )
# if uploaded_file:
#     if st.button("Process PDF"):
#         with st.spinner("Processing PDF..."):
#             process_uploaded_pdf(uploaded_file)
#         st.success("✅ PDF processed successfully!")
# # -----------------------------
# # Load FAISS Database
# # -----------------------------
# if st.button("Load PDF"):
#     st.session_state.db = load_vector_store()
#     st.success("✅ PDF Loaded Successfully!")
# # -----------------------------
# # Chat Section
# # -----------------------------
# if "db" in st.session_state:
#     question = st.chat_input("Ask anything about your PDF")
#     if question:
#         # Store User Message
#         st.session_state.messages.append(
#             {
#                 "role": "user",
#                 "content": question
#             }
#         )
#         docs = st.session_state.db.similarity_search(
#             question,
#             k=5
#         )
#         context = "\n\n".join(
#             doc.page_content
#             for doc in docs
#         )
#         with st.spinner("🤖 Gemini is thinking..."):
#             answer = ask_gemini(
#                 context,
#                 question
#             )
#         # Store AI Message
#         st.session_state.messages.append(
#             {
#                 "role": "assistant",
#                 "content": answer
#             }
#         )
#     # Display Complete Chat History
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.write(message["content"])

# import streamlit as st
# from pdf_processor import process_uploaded_pdf
# from vector_store import load_vector_store
# from chatbot import ask_gemini
# st.set_page_config(
#     page_title="AI PDF Chatbot",
#     page_icon="📄",
#     layout="wide"
# )
# st.title("📄 AI PDF Chatbot")
# # -----------------------------
# # Chat History
# # -----------------------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# # -----------------------------
# # Upload PDF
# # -----------------------------
# uploaded_file = st.file_uploader(
#     "Upload a PDF",
#     type=["pdf"]
# )
# if uploaded_file:
#     if st.button("Process PDF"):
#         with st.spinner("Processing PDF..."):
#             process_uploaded_pdf(uploaded_file)
#         st.success("✅ PDF processed successfully!")
# # -----------------------------
# # Load FAISS
# # -----------------------------
# if st.button("Load PDF"):
#     st.session_state.db = load_vector_store()
#     st.success("✅ PDF Loaded Successfully!")
# # -----------------------------
# # Chat
# # -----------------------------
# if "db" in st.session_state:
#     question = st.chat_input("Ask anything about your PDF")
#     if question:
#         docs = st.session_state.db.similarity_search(
#             question,
#             k=5
#         )
#         context = "\n\n".join(
#             doc.page_content
#             for doc in docs
#         )
#         pages = sorted(
#             list(
#                 {
#                     doc.metadata["page"]
#                     for doc in docs
#                 }
#             )
#         )
#         answer = ask_gemini(
#             context,
#             question
#         )
#         st.session_state.messages.append(
#             {
#                 "role": "user",
#                 "content": question
#             }
#         )
#         source_text = "\n\n📄 **Sources:**\n"
#         for page in pages:
#             source_text += f"- Page {page}\n"
#         st.session_state.messages.append(
#             {
#                 "role": "assistant",
#                 "content": answer + source_text
#             }
#         )
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])


# from quiz import generate_quiz
# import streamlit as st
# from pdf_processor import process_uploaded_pdf
# from vector_store import load_vector_store
# from chatbot import ask_gemini
# from summary import generate_summary
# st.set_page_config(
#     page_title="AI Study Assistant",
#     page_icon="📚",
#     layout="wide"
# )
# # --------------------------
# # Session State
# # --------------------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# if "db" not in st.session_state:
#     st.session_state.db = None
# # --------------------------
# # Sidebar
# # --------------------------
# with st.sidebar:
#     st.title("📚 AI Study Assistant")
#     uploaded_file = st.file_uploader(
#         "Upload PDF",
#         type=["pdf"]
#     )
#     if uploaded_file:
#         st.success(f"📂 {uploaded_file.name}")
#         if st.button("Process PDF"):
#             with st.spinner("Processing PDF..."):
#                 process_uploaded_pdf(uploaded_file)
#             st.session_state.db = load_vector_store()
#             st.success("✅ PDF Ready!")
#     st.divider()
#     if st.button("🧹 Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()
#     st.divider()
#     st.subheader("ℹ️ Project Information")
#     st.write("**Embedding Model**")
#     st.caption("all-MiniLM-L6-v2")
#     st.write("**Vector Database**")
#     st.caption("FAISS")
#     st.write("**LLM**")
#     st.caption("Gemini 2.5 Flash")
# # --------------------------
# # Main Window
# # --------------------------
# st.title("💬 AI Study Assistant")
# if st.session_state.db:
#     # --------------------------
#     # Summary Button
#     # --------------------------
#     if st.button("📄 Generate Summary"):
#         docs = st.session_state.db.similarity_search(
#             "Summarize the whole document",
#             k=20
#         )
#         context = "\n\n".join(
#             doc.page_content
#             for doc in docs
#         )
#         with st.spinner("Generating Summary..."):
#             summary = generate_summary(context)
#         st.subheader("📄 Document Summary")
#         st.write(summary)
#     # --------------------------
#     # Generate Quiz
#     # --------------------------
#     if st.button("❓ Generate Quiz"):
#         docs = st.session_state.db.similarity_search(
#             "Generate quiz from the document",
#             k=20
#         )
#         context = "\n\n".join(
#             doc.page_content
#             for doc in docs
#         )
#         with st.spinner("Generating Quiz..."):
#             quiz = generate_quiz(context)
#         st.subheader("❓ Quiz")
#         st.write(quiz)
#     # --------------------------
#     # Chat
#     # --------------------------
#     question = st.chat_input(
#         "Ask anything about your PDF..."
#     )
#     if question:
#         docs = st.session_state.db.max_marginal_relevance_search(
#             question,
#             k=5,
#             fetch_k=15
#         )
#         context = "\n\n".join(
#             doc.page_content
#             for doc in docs
#         )
#         pages = sorted(
#             {
#                 doc.metadata["page"]
#                 for doc in docs
#             }
#         )
#         answer = ask_gemini(
#             context,
#             question
#         )
#         sources = "\n\n📄 **Sources**\n"
#         for page in pages:
#             sources += f"- Page {page}\n"
#         st.session_state.messages.append(
#             {
#                 "role": "user",
#                 "content": question
#             }
#         )
#         st.session_state.messages.append(
#             {
#                 "role": "assistant",
#                 "content": answer + sources
#             }
#         )
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])
# else:
#     st.info("⬅️ Upload and process a PDF to begin.")

# import streamlit as st
# from pdf.pdf_processor import process_uploaded_pdf
# from database.vector_store import load_vector_store
# from core.chatbot import ask_gemini
# from core.summary import generate_summary
# from core.quiz import generate_quiz
# from core.notes import generate_notes
# from core.flashcards import generate_flashcards
# from core.interview import generate_interview_questions
# st.set_page_config(
#     page_title="AI Study Assistant",
#     page_icon="📚",
#     layout="wide"
# )
# st.title("📚 AI Study Assistant")
# st.info(
#     "Project successfully refactored into a professional folder structure!"
# )

# import streamlit as st
# from ui.sidebar import show_sidebar
# from ui.dashboard import show_dashboard
# from ui.chat import display_chat
# st.set_page_config(
#     page_title="AI Study Assistant",
#     page_icon="📚",
#     layout="wide"
# )
# # -------------------------
# # Session State
# # -------------------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# # -------------------------
# # Dashboard
# # -------------------------
# show_dashboard()
# # -------------------------
# # Sidebar
# # -------------------------
# uploaded_file, clear_chat = show_sidebar()
# # -------------------------
# # Clear Chat
# # -------------------------
# if clear_chat:
#     st.session_state.messages = []
#     st.rerun()
# # -------------------------
# # Display Chat
# # -------------------------
# display_chat(st.session_state.messages)

import streamlit as st
from pdf.pdf_processor import process_uploaded_pdf
from database.vector_store import load_vector_store
from core.chatbot import ask_gemini
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
    st.caption("Gemini 2.5 Flash")
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
        with st.spinner("🤖 Gemini is thinking..."):
            try:
                answer = ask_gemini(
                    context,
                    question
                )
            except Exception as e:
                st.error(
                    f"❌ Gemini Error:\n\n{e}"
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
    "🚀 Built by Dinesh Namburi | Powered by Streamlit • LangChain • FAISS • Hugging Face • Gemini 2.5 Flash"
)