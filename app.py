import gradio as gr
from langchain_ollama import OllamaLLM

# Initialize the language model using the same model as tests/hello_world.py
llm = OllamaLLM(model="llama3.2")

def generate_response(prompt: str) -> str:
    """Return a completion from the Ollama model."""
    return llm.invoke(prompt)

# Basic Gradio interface with a text box for the prompt
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here"),
    outputs="text",
    title="Party Planner Chat",
)

if __name__ == "__main__":
    interface.launch()
