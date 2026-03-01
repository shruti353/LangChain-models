from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini',temperature=1.5, max_tokens=100)
result = model.invoke("Explain what an LLM is in simple words.")
print(result.content)