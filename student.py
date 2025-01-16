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
You're a student learning Kubernetes.
1. Join https://webchat.quakenet.org/, choose a short nickname, and join the #kubernetes channel.
2. Wait for the teacher to offer their help.
3. Once help is offered, ask a simple Kubernetes question.
4. Thank the teacher after getting an answer, and then leave the channel.
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
