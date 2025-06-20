from langchain_community.llms import Ollama

via `ollama pull`
llm = Ollama(model="llama3.2")

response = llm.invoke("Tell me a monkey fact!")
print(response)