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


def generate_chat_response(
    message: str,
    history: list[tuple[str, str]],
    title: str,
    date_time: str,
    street: str,
    city: str,
    state_field: str,
    zip_code: str,
    country: str,
    description: str,
) -> tuple[str, list[tuple[str, str]]]:
    """Return a chat completion from the Ollama model using event context."""

    address = Address(
        street=street, city=city, state=state_field, zip_code=zip_code, country=country
    )
    conversation = "\n".join(f"User: {user}\nAI: {bot}" for user, bot in history)
    full_prompt = (
        f"Event Title: {title}\nDate: {date_time}\nLocation: {address}\n"
        f"Description: {description}\n\n{conversation}\nUser: {message}\nAI:"
    )
    response = llm.invoke(full_prompt)
    history.append((message, response))
    return "", history


def build_interface() -> gr.Blocks:
    """Create the Gradio Blocks interface with a chat dialogue."""

    with gr.Blocks(title="Party Planner Chat") as demo:
        with gr.Row():
            with gr.Column():
                title = gr.Textbox(label="Event Title")
                date_time = gr.components.DateTime(label="Date & Time")
                street = gr.Textbox(label="Street Address")
                city = gr.Textbox(label="City")
                state_field = gr.Textbox(label="State")
                zip_code = gr.Textbox(label="ZIP Code")
                country = gr.Textbox(label="Country")
                description = gr.Textbox(label="Description", lines=4)
        chatbot = gr.Chatbot(type="messages")
        message = gr.Textbox(label="Your Message")
        send = gr.Button("Send")
        send.click(
            generate_chat_response,
            inputs=[
                message,
                chatbot,
                title,
                date_time,
                street,
                city,
                state_field,
                zip_code,
                country,
                description,
            ],
            outputs=[message, chatbot],
        )
    return demo


interface = build_interface()

if __name__ == "__main__":
    build_interface().launch(share=True)
