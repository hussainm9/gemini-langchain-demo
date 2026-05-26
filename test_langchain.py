from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

response = llm.invoke('tell me about yourself how to answer this question for a 3 year career gap after graduation')
print(response.text)