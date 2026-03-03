from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='meta-llama/Meta-Llama-3-8B-Instruct',
    task='text-generation',
    max_new_tokens=200,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Explain what an LLM is in simple words.")

print(result.content)