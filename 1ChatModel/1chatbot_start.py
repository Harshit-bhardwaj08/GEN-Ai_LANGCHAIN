""" 
YOU
 ↓
LangChain
 ↓
(Decision)
 ↓
Weather API call
 ↓
Live Weather Data
 ↓
LangChain
 ↓
Gemini
 ↓
Final Answer
 ↓
YOU


STEP-BY-STEP (Very Easy)
1️⃣ Tum bolte ho
"Delhi ka weather batao"

2️⃣ LangChain kya karta hai? 🤖

LangChain sochta hai:

❓ Question kis type ka hai?
→ Weather
→ Mujhe external data chahiye

3️⃣ LangChain WEATHER API call karta hai 🌦️
OpenWeather API
 ↓
Temperature
Humidity
Rain
Wind


📌 YEH WEB API CALL HAI
👉 Gemini se pehle hoti hai

4️⃣ Data clean hota hai
Raw JSON
 ↓
Readable Text


Example:

Temperature: 32°C
Humidity: 60%
Rain: No

5️⃣ Ab Gemini ko smart prompt diya jaata hai
"Based on this data:
Temperature 32°C, Humidity 60%,
Explain weather in simple Hindi."


📌 Yahan Gemini API call hoti hai

6️⃣ Gemini natural language answer deta hai
"Aaj Delhi me garmi hai,
barish ke chances kam hain."

🧠 FINAL FLOW (Yaad rakhne layak)
User Question
 ↓
LangChain Brain
 ↓
Weather API (Internet)
 ↓
Real Data
 ↓
Gemini (Language)
 ↓
Human Answer
 """


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest"
)

result = llm.invoke("What is the square root of 49?")
print(result.content)
 