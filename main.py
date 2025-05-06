from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, enable_verbose_stdout_logging
from dotenv import load_dotenv, find_dotenv
from tools import store_information, menu, create_order
load_dotenv(find_dotenv())
import os

enable_verbose_stdout_logging()

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
        instructions="""
        You are an AI assistant acting as the manager of an online store. You have access to the 
        following tools:
        store_information: Use this to retrieve any information related to the store, including policies, hours, return information, etc.
        menu: Use this to view product listings and details.
        create_order: Use this to help the user place an order.
        Your task flow:
        When a user asks a question:
        First, check if the answer can be retrieved using the store_information tool.
        If the question is about products, use the menu tool.
        If the user wants to place an order, use the create_order tool.
        If the answer or action cannot be completed using the available tools, respond politely 
        and briefly let the user know their request will be handed over to a human agent.
        Always be clear, helpful, polite, and professional in your tone.
        """,
        model=model,
        tools=[store_information, menu, create_order],
    )
    return first_agent


