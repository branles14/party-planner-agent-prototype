from dataclasses import dataclass

import gradio as gr
from langchain_ollama import OllamaLLM

# Initialize the language model using the same model as tests/hello_world.py
llm = OllamaLLM(model="llama3.2")


@dataclass
class Address:
    """Simple container for address components."""

    street: str
    city: str
    state: str
    zip_code: str
    country: str

    def __str__(self) -> str:
        return (
            f"{self.street}, {self.city}, {self.state} {self.zip_code}, {self.country}"
        )


def generate_response(
    title: str,
    date_time: str,
    street: str,
    city: str,
    state: str,
    zip_code: str,
    country: str,
    description: str,
    prompt: str,
) -> str:
    """Return a completion from the Ollama model using event context."""

    address = Address(
        street=street, city=city, state=state, zip_code=zip_code, country=country
    )
    full_prompt = (
        f"Event Title: {title}\nDate: {date_time}\nLocation: {address}\n"
        f"Description: {description}\n\nUser Prompt: {prompt}"
    )
    return llm.invoke(full_prompt)


# Basic Gradio interface with a text box for the prompt
interface = gr.Interface(
    fn=generate_response,
    inputs=[
        gr.Textbox(label="Event Title"),
        gr.components.DateTime(label="Date & Time"),
        gr.Textbox(label="Street Address"),
        gr.Textbox(label="City"),
        gr.Textbox(label="State"),
        gr.Textbox(label="ZIP Code"),
        gr.Textbox(label="Country"),
        gr.Textbox(label="Description", lines=4),
        gr.Textbox(label="Prompt"),
    ],
    outputs="text",
    title="Party Planner Chat",
)

if __name__ == "__main__":
    interface.launch(share=True)
