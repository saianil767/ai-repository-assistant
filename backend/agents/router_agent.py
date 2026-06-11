import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def route_question(question):

    keywords = [
        "repository",
        "repo",
        "class",
        "function",
        "module",
        "file",
        ".py",
        "architecture",
        "documentindex",
        "recordmanager"
    ]

    q = question.lower()

    for word in keywords:

        if word in q:
            return "repo"

    prompt = f"""
Classify the question into one category.

repo:
Questions about source code, classes,
functions, repositories, github projects,
architecture, modules and files.

pdf:
Questions about uploaded documents.

general:
General knowledge questions.

Question:
{question}

Return only one word:
repo, pdf, or general
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

    return response.choices[0].message.content.strip().lower()