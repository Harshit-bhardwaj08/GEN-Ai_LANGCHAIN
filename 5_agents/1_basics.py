from dotenv import load_dotenv
import datetime

from langchain.agents import initialize_agent, AgentType, tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# -------- TOOL --------
@tool
def get_system_time(format: str = "%H:%M:%S"):
    """Returns the current time in the specified format"""
    return datetime.datetime.now().strftime(format)

# -------- LLM --------
llm = ChatGoogleGenerativeAI(
    model="",
    temperature=0
)

# -------- QUERY --------
query = "What is the current time in London? (You are in India). Just show the time, not the date."

# -------- TOOLS --------
tools = [get_system_time]

# -------- AGENT (ReAct happens internally) --------
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# -------- RUN --------
agent.invoke(query)
