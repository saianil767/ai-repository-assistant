from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


def create_vector_store(chunks):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    return vectorstore