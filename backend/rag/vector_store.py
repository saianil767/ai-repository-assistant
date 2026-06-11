import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma


embedding_model = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def create_vector_store(chunks):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    return vectorstore