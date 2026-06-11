import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_rag_answer(question, docs):

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a helpful AI assistant.

Answer the question using ONLY the provided context.

Provide a detailed answer.
Include all important points from the context.
If the context contains multiple sections, summarize each section.
Do not give a short answer unless the context itself is short.

Context:
{context}

Question:
{question}

Detailed Answer:
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