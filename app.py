import gradio as gr
from langchain_ollama import OllamaLLM

# Initialize the language model using the same model as tests/hello_world.py
llm = OllamaLLM(model="llama3.2")

def generate_response(
    title: str, date: str, time: str, description: str, prompt: str
) -> str:
    """Return a completion from the Ollama model using event context."""
    full_prompt = (
        f"Event Title: {title}\nDate: {date}\nTime: {time}\n"
        f"Description: {description}\n\nUser Prompt: {prompt}"
    )
    return llm.invoke(full_prompt)

# Basic Gradio interface with a text box for the prompt
interface = gr.Interface(
    fn=generate_response,
    inputs=[
        gr.Textbox(label="Event Title"),
        gr.components.DateTime(label="Date"),
        gr.Textbox(label="Description", lines=2),
        gr.Textbox(lines=2, placeholder="Enter your prompt here", label="Prompt"),
    ],
    outputs="text",
    title="Party Planner Chat",
)

if __name__ == "__main__":
    interface.launch(share=True)
