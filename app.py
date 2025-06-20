from dataclasses import dataclass
import json
import re

import gradio as gr
from gradio.components.chatbot import ChatMessage
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
    history: list[ChatMessage | dict],
    title: str,
    date_time: str,
    street: str,
    city: str,
    state_field: str,
    zip_code: str,
    country: str,
    description: str,
) -> tuple[str, list[ChatMessage], dict]:
    """Return a chat completion from the Ollama model using event context."""

    address = Address(
        street=street, city=city, state=state_field, zip_code=zip_code, country=country
    )
    conversation_lines: list[str] = []
    for msg in history:
        if isinstance(msg, dict):
            role = msg.get("role", "assistant")
            content = msg.get("content", "")
        else:
            role = msg.role
            content = msg.content
        speaker = "User" if role == "user" else "AI"
        conversation_lines.append(f"{speaker}: {content}")
    conversation = "\n".join(conversation_lines)
    instruction = (
        "After your main reply, provide a JSON object with any proposed event field "
        "updates. Use keys: title, date_time, street, city, state, zip_code, "
        "country, description. If no change, use null or omit the key."
    )
    full_prompt = (
        f"Event Title: {title}\nDate: {date_time}\nLocation: {address}\n"
        f"Description: {description}\n\n{conversation}\nUser: {message}\nAI: {instruction}"
    )
    response = llm.invoke(full_prompt)

    suggestions: dict = {}
    reply_text = response
    fence_match = re.search(r"```json\s*(\{.*?\})\s*```", response, re.S)
    json_text = None
    if fence_match:
        json_text = fence_match.group(1)
        reply_text = response.replace(fence_match.group(0), "").strip()
    else:
        brace_match = re.search(r"\{.*\}", response, re.S)
        if brace_match:
            json_text = brace_match.group(0)
            reply_text = response[: brace_match.start()].strip()
    if json_text:
        try:
            suggestions = json.loads(json_text)
        except json.JSONDecodeError:
            suggestions = {}

    history.append(ChatMessage(content=message, role="user"))
    history.append(ChatMessage(content=reply_text, role="assistant"))
    return "", history, suggestions


def apply_suggestions(
    suggestions: dict,
    title: str,
    date_time: str,
    street: str,
    city: str,
    state_field: str,
    zip_code: str,
    country: str,
    description: str,
) -> tuple:
    """Apply suggested fields if provided and clear the suggestions box."""
    title_val = suggestions.get("title", title) if suggestions else title
    date_val = suggestions.get("date_time", date_time) if suggestions else date_time
    street_val = suggestions.get("street", street) if suggestions else street
    city_val = suggestions.get("city", city) if suggestions else city
    state_val = suggestions.get("state", state_field) if suggestions else state_field
    zip_val = suggestions.get("zip_code", zip_code) if suggestions else zip_code
    country_val = suggestions.get("country", country) if suggestions else country
    desc_val = (
        suggestions.get("description", description) if suggestions else description
    )
    return (
        gr.update(value=title_val),
        gr.update(value=date_val),
        gr.update(value=street_val),
        gr.update(value=city_val),
        gr.update(value=state_val),
        gr.update(value=zip_val),
        gr.update(value=country_val),
        gr.update(value=desc_val),
        gr.update(value=None),
    )


def reject_suggestions(_: dict):
    """Clear suggestions without applying them."""
    return gr.update(value=None)


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
        suggestions_box = gr.JSON(label="Proposed Updates")
        with gr.Row():
            accept_btn = gr.Button("Accept")
            reject_btn = gr.Button("Reject")
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
            outputs=[message, chatbot, suggestions_box],
        )
        accept_btn.click(
            apply_suggestions,
            inputs=[
                suggestions_box,
                title,
                date_time,
                street,
                city,
                state_field,
                zip_code,
                country,
                description,
            ],
            outputs=[
                title,
                date_time,
                street,
                city,
                state_field,
                zip_code,
                country,
                description,
                suggestions_box,
            ],
        )
        reject_btn.click(
            reject_suggestions,
            inputs=[suggestions_box],
            outputs=[suggestions_box],
        )
    return demo


interface = build_interface()

if __name__ == "__main__":
    build_interface().launch(share=True)
