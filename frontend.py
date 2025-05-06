import chainlit as cl
from main import main as get_agent
from agents import Runner

@cl.on_chat_start
def start_chat():
    # Initialize the agent when the chat starts
    cl.user_session.agent = get_agent()
    cl.user_session.history = []


@cl.on_message
async def main(message: cl.Message):
    # frontend code to handle the message from the user
    history = cl.user_session.history
    history.append({"role": "user", "content": message.content})
    first_agent = cl.user_session.agent
    response = Runner.run_sync(
        starting_agent= first_agent,
        input=history
    )
    await cl.Message(content=response.final_output).send()
    history.append({"role": "assistant", "content": response.final_output})
    cl.user_session.history = history