from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# 1. CHANGE THE IMPORT
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv

load_dotenv()

# 2. CHANGE THE MODEL SETUP
# We use "gemini-flash-latest" because you confirmed it works with your free tier
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest", 
    temperature=0
)

messages = [
    SystemMessage(content="You are an expert in social media content strategy"),
    HumanMessage(content="Give a short tip to create engaging posts on Instagram"),
    AIMessage(content="**Focus on the first three seconds:** Use a strong visual hook (a captivating image or the most interesting part of a video) and a punchy opening line in your caption to immediately grab attention and stop the scroll."),
    HumanMessage(
        content="Using the previous tip about the first three seconds, can you explain how to use storytelling in Instagram posts?"
    )
]

# 3. RUN IT
result = llm.invoke(messages)
print(result.content)