import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_repo_answer(question, docs):

    context = "\n\n".join(
         [doc.page_content[:1000] for doc in docs]
    )

    prompt = f"""
You are a senior software engineer.

Answer the question based only on the repository code below.

Repository Context:

{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content