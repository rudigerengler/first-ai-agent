# My First AI Agent

A simple AI agent built with Python, Hugging Face's `smolagents` framework, and OpenAI's API. This project explores how AI agents can reason, execute tools, and interact with external information.

## Features

- **Web Search:** Searches the internet using DuckDuckGo to answer questions.
- **Time-Zone Tool:** Retrieves the current local time in different time zones.
- **AI Reasoning:** Uses an OpenAI language model (`gpt-4.1-mini`) to decide when and how to use tools.
- **Web Interface:** Provides a simple interactive interface built with Gradio.

## Tech Stack

- Python
- Hugging Face `smolagents`
- OpenAI API
- Gradio
- DuckDuckGo Search
- `pytz`

## How It Works

1. The user submits a question through the Gradio interface.
2. The AI agent interprets the question and determines whether tools are needed.
3. The agent executes the relevant tools and processes their outputs.
4. The final answer is displayed in the interface.

## Running Locally

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/first-ai-agent.git
cd first-ai-agent
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
```

On Windows (Command Prompt):

```cmd
.venv\Scripts\activate.bat
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Configure your OpenAI API key**

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Never commit your actual API key to GitHub.

**5. Launch the application**

```bash
python ui.py
```

Open the local Gradio URL shown in your terminal.

## Project Structure

```text
first-ai-agent/
├── tools/
│   └── time_tool.py
├── app.py
├── ui.py
├── requirements.txt
├── .env          # Local only, not committed
├── .gitignore
└── README.md
```

## What I Learned

This project provided practical experience with:

- Building AI agents using `smolagents`.
- Integrating custom and third-party tools.
- Understanding the agent reasoning and tool-execution loop.
- Separating backend logic from the user interface.
- Managing Python dependencies, environment variables, and API credentials.

## Future Improvements

- Add more custom tools and capabilities.
- Improve error handling and reliability.
- Introduce conversational memory.
- Explore more advanced agent architectures.
