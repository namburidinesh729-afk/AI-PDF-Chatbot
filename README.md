# 📚 AI Study Assistant
An AI-powered **PDF Study Assistant** built using **Python, Streamlit, LangChain, FAISS, Hugging Face Embeddings, and Google Gemini 2.5 Flash**.
Upload any PDF and instantly interact with it using AI.
---
# 🚀 Live Demo
🌐 https://ai-study-assistant-dinesh.streamlit.app
---
# 📂 GitHub Repository
💻 https://github.com/namburidinesh729-afk/AI-PDF-Chatbot
---
# ✨ Features
- 📄 Upload PDF documents
- 💬 Chat with your PDF
- 🔍 Semantic Search using FAISS
- 📑 Source Page References
- 📄 AI Summary Generation
- ❓ Multiple Choice Quiz Generation
- 📝 Revision Notes Generation
- 🧠 Flashcard Generation
- 🎯 Interview Question Generation
- 📥 Download Generated Content
---
# 📸 Screenshots
> Add screenshots of:
- Home Page
- PDF Upload
- Chat Interface
- Summary
- Quiz
- Notes
- Flashcards
---
# 🛠 Tech Stack
| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| LangChain | RAG Pipeline |
| FAISS | Vector Database |
| Hugging Face Embeddings | Text Embeddings |
| Google Gemini 2.5 Flash | Large Language Model |
| PyPDF2 | PDF Processing |
---
# 🏗 Project Architecture
```text
          User Uploads PDF
                  │
                  ▼
            PDF Processing
                  │
                  ▼
          Text Chunking
                  │
                  ▼
     Hugging Face Embeddings
                  │
                  ▼
          FAISS Vector Store
                  │
                  ▼
          User Question
                  │
                  ▼
         MMR Retrieval Search
                  │
                  ▼
       Gemini 2.5 Flash LLM
                  │
                  ▼
      AI Answer + Source Pages
```
---
# 📂 Project Structure
```
AI-PDF-Chatbot/
│
├── app.py
├── core/
│   ├── chatbot.py
│   ├── summary.py
│   ├── quiz.py
│   ├── notes.py
│   ├── flashcards.py
│   └── interview.py
├── database/
│   └── vector_store.py
├── pdf/
│   ├── pdf_processor.py
│   ├── text_splitter.py
│   └── utils.py
├── ui/
├── requirements.txt
└── README.md
```
---
# ⚙ Installation
```bash
git clone https://github.com/namburidinesh729-afk/AI-PDF-Chatbot.git
cd AI-PDF-Chatbot
pip install -r requirements.txt
streamlit run app.py
```
---
# 🎯 Future Improvements
- 🔊 Voice-based Chat
- 🌐 Multi-language Support
- 📚 Multiple PDF Chat
- 🖼 Image OCR Support
- 📊 Progress Tracking
- 🔑 User Authentication
---
# 👨‍💻 Author
**Dinesh Namburi**
B.Tech Student | AI & Python Enthusiast
GitHub:
https://github.com/namburidinesh729-afk
---
⭐ If you like this project, consider giving it a **Star** on GitHub.
