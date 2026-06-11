from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="code_db",
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


def retrieve_code(question):

    docs = retriever.invoke(question)

    return docs