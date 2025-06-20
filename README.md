# Party Planner AI Agent 🎉🤖

An intelligent event co-host that enhances human-created event listings with AI-powered suggestions, contextual awareness, and automation. Built with Gradio + LangChain + Ollama.

## ✨ Features

- 📝 **Event Config Interface**: Clean separation of user-defined event details
- 🤖 **AI Agent Panel**:
  - Rewrite event descriptions with custom tone
  - Suggest cover image prompts using event + weather context
  - Simulate RSVP messages for UX testing
  - Recommend alternate venues if needed
  - Generate shopping lists with affiliate links

## 🛠 Tech Stack

- Python 3
- [Gradio](https://www.gradio.app/) (UI)
- [LangChain](https://www.langchain.com/) + `langchain_ollama`
- LLM: `llama3.2` via Ollama backend

## 🚀 Running the App

```bash
pip install -r requirements.txt
python app.py