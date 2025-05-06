from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
import os

# Disable tracing for the entire script
set_tracing_disabled(True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

def main():
    external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )
    first_agent = Agent(
        name="First Agent",
        instructions="You are a helpful assistant.",
        model=model,
    )
    return first_agent


