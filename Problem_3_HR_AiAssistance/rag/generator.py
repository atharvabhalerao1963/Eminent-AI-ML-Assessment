from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class HRGenerator:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0
        )

    def generate(self, prompt: str):

        response = self.llm.invoke(prompt)

        return response.content