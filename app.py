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


def build_interface() -> gr.Blocks:
    """Create the Gradio interface with separate columns."""
    with gr.Blocks(title="Party Planner Chat") as demo:
        with gr.Row():
            with gr.Column():
                title = gr.Textbox(label="Event Title")
                date_time = gr.components.DateTime(label="Date & Time")
                street = gr.Textbox(label="Street Address")
                city = gr.Textbox(label="City")
                state = gr.Textbox(label="State")
                zip_code = gr.Textbox(label="ZIP Code")
                country = gr.Textbox(label="Country")
                description = gr.Textbox(label="Description", lines=4)
            with gr.Column():
                prompt = gr.Textbox(label="Prompt")
                output = gr.Textbox(label="Response", lines=10)
                run_btn = gr.Button("Submit")

        run_btn.click(
            generate_response,
            inputs=[
                title,
                date_time,
                street,
                city,
                state,
                zip_code,
                country,
                description,
                prompt,
            ],
            outputs=output,
        )

    return demo


if __name__ == "__main__":
    build_interface().launch(share=True)
