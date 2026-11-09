
import os


from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIModel, tool, DuckDuckGoSearchTool
from tools.time_tool import get_current_time_in_timezone

load_dotenv()


model = OpenAIModel(
    model_id = "gpt-4.1-mini",
    api_key = os.environ["OPENAI_API_KEY"],
    max_tokens = 1000,
)


agent = CodeAgent(
    model = model,
    tools = [
        get_current_time_in_timezone,
        DuckDuckGoSearchTool()
        ],
    max_steps = 3,
    verbosity_level = 1,
)

if __name__ == "__main__":
    result = agent.run(
        "Search the web for the winner of the 2025 Formula 1 "
        "World Drivers Championship. "
        "Use the search results to identify the winner."
    )

    

    print("Final answer:", result)

