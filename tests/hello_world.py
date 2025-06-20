from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")
response = llm.invoke("Give me a monkey fact.")
print(response)
