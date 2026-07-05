import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

print("Key exists:", os.getenv("GOOGLE_API_KEY") is not None)
print("Key prefix:", os.getenv("GOOGLE_API_KEY")[:8])

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

response = llm.invoke("Say Hello")

print(response.content)