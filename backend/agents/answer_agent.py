import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(question: str):
    try:
        print("Question:", question)

        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": question}
            ],
            model="llama-3.3-70b-versatile"
        )

        print("Success!")

        return response.choices[0].message.content

    except Exception as e:
        print("ERROR OCCURRED:")
        print(type(e))
        print(e)
        return str(e)