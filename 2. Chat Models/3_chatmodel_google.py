from langchain_google_generativeai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model =ChatGoogleGenerativeAI(model='gemini-2.0-pro', temperature=1.5, max_tokens=100)

result = model.invoke('Explain what an LLM is in simple words.')
print(result.content)

