import os

from langchain_core.documents import Document
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def load_python_files(repo_path):

    documents = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):

                file_path = os.path.join(
                    root,
                    file
                )

                try:

                    with open(
                        file_path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        content = f.read()

                        docs = splitter.create_documents(
                            [content]
                        )

                        for doc in docs:

                            doc.metadata = {
                                "source": file_path
                            }

                            documents.append(doc)

                except Exception:

                    pass

    return documents