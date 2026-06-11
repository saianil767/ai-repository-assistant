from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


def create_code_vectorstore(documents):

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory="code_db"
    )

    return vectorstore