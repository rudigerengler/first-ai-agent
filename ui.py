import gradio as gr
from app import agent


def ask_agent(question):
    result = agent.run(question)
    return str(result)   


demo = gr.Interface(
    fn=ask_agent,
    inputs=gr.Textbox(label="Ask your AI Agent"),
    outputs=gr.Textbox(label="Agent Response"),
    title="My First AI Agent",
    description="An AI agent powered by OpenAI, with web search and time-zone tools."
)

if __name__ == "__main__":
    demo.launch(inbrowser=True)