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

Set model="llama3.2" or update the model name based on your Ollama config.

📦 Roadmap

[ ] Add real-time weather API integration

[ ] Implement AI-generated cover image

[ ] Guest message queue + host-side relay

[ ] Alt venue suggester (based on map data)


❤️ Vision

To build a flexible, respectful AI assistant that collaborates with the event host—not overrides them. The goal is smarter planning, not automated replacement.


---

Built for fun, function, and maybe to impress someone.