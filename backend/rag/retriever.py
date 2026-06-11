import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma


def retrieve_docs(question):

    embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 20}
    )

    docs = retriever.invoke(question)

    return docs