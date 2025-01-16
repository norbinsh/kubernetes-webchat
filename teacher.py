from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the .env file.")

llm = ChatOpenAI(model="gpt-4o", api_key=api_key)

TASK_DESCRIPTION = """
You're a Kubernetes teacher.
1. Join https://webchat.quakenet.org/, choose a short nickname, and join the #kubernetes channel.
2. Accept forms if they come your way.
3. Wait for the student to join the channel.
4. Once the student joins, offer your help by sending a message.
5. Wait for the student to ask a question.
6. Answer the question, wait for thanks, and then leave the channel.
"""

async def main() -> None:
    try:
        agent = Agent(task=TASK_DESCRIPTION, llm=llm)
        result = await agent.run()
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
