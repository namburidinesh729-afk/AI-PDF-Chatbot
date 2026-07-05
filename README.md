# 📚 AI Study Assistant
An AI-powered Study Assistant built using **Python, Streamlit, LangChain, FAISS, Hugging Face Embeddings, and Google Gemini**.
This application allows users to upload PDF documents and interact with them using AI.
---
## 🚀 Features
- 📂 Upload PDF
- 💬 Chat with PDF
- 📄 AI Summary Generator
- ❓ Quiz Generator
- 📝 Smart Notes Generator
- 🧠 Flashcard Generator
- 🎯 Interview Question Generator
- 📄 Source References
- ⬇ Download Generated Results
---
## 🛠 Technologies Used
- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face Embeddings
- Google Gemini API
- PyPDF
- Sentence Transformers
---
## 📂 Project Structure
```
AI-PDF-Chatbot/
│
├── app.py
├── core/
├── database/
├── pdf/
├── ui/
├── pdfs/
├── faiss_index/
├── requirements.txt
└── README.md
```
---
## ⚙ Installation
Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/AI-PDF-Chatbot.git
```
Move into the project
```bash
cd AI-PDF-Chatbot
```
Create a virtual environment
```bash
python -m venv venv
```
Activate it
Mac/Linux
```bash
source venv/bin/activate
```
Windows
```bash
venv\Scripts\activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
Create a `.env` file
```text
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```
Run the application
```bash
streamlit run app.py
```
---
## 📸 Screenshots
(Add screenshots here after uploading to GitHub.)
---
## 👨‍💻 Author
**Dinesh Namburi**