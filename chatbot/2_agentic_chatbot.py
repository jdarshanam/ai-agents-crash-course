import chainlit as cl
import dotenv

dotenv.load_dotenv()

from agents import Runner
from nutrition_agent import nutrition_agent

@cl.on_message
async def on_message_respond(msg: cl.Message):
    res = await Runner.run(nutrition_agent,msg.content)
    await cl.Message(content=res.final_output).send()

