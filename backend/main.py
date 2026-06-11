from fastapi import FastAPI, UploadFile, File
import shutil
import os

from backend.models import QuestionRequest
from backend.agents.answer_agent import generate_answer

from backend.rag.retriever import retrieve_docs
from backend.agents.rag_agent import generate_rag_answer
from backend.rag.pdf_loader import load_pdf
from backend.rag.vector_store import create_vector_store
from backend.github.code_retriever import retrieve_code
from backend.agents.github_agent import generate_repo_answer
from backend.graph import graph
from pydantic import BaseModel

from backend.github.repo_loader import clone_repo
from backend.github.code_loader import load_python_files
from backend.github.code_vector_store import create_code_vectorstore

from backend.agents.general_agent import (
    generate_general_answer
)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Repository Assistant API Running"
    }


@app.post("/query")
def query(request: QuestionRequest):

    answer = generate_answer(request.question)

    return {
        "question": request.question,
        "answer": answer
    }


@app.post("/upload-pdf")
def upload_pdf(file: UploadFile = File(...)):

    # Create uploads folder if it doesn't exist
    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    chunks = load_pdf(file_path)

    chunks = chunks[:10]

    create_vector_store(chunks)



    return {
        "message": f"{file.filename} uploaded successfully",
        "chunks_created": len(chunks)
    }
@app.post("/ask-pdf")
def ask_pdf(request: QuestionRequest):

    docs = retrieve_docs(request.question)

    answer = generate_rag_answer(
        request.question,
        docs
    )

    return {
        "question": request.question,
        "answer": answer
    }
@app.post("/ask-repo")
def ask_repo(request: QuestionRequest):

    docs = retrieve_code(
        request.question
    )

    answer = generate_repo_answer(
        request.question,
        docs
    )

    return {
        "question": request.question,
        "answer": answer
    }
@app.post("/smart-query")
def smart_query(request: QuestionRequest):

    result = graph.invoke(
        {
            "question": request.question
        }
    )

    route = result["route"]

    if route == "pdf":

        docs = retrieve_docs(
            request.question
        )

        answer = generate_rag_answer(
            request.question,
            docs
        )

    elif route == "repo":

        try:

            docs = retrieve_code(
                request.question
            )

            answer = generate_repo_answer(
                request.question,
                docs
            )

        except Exception as e:

            answer = str(e)

    else:

        answer = generate_general_answer(
            request.question
        )

    return {
        "route": route,
        "question": request.question,
        "answer": answer
    }
class RepoRequest(BaseModel):
    github_url: str
@app.post("/process-repo")
def process_repo(request: RepoRequest):

    repo_path = clone_repo(
        request.github_url
    )

    files = load_python_files(
        repo_path
    )

    create_code_vectorstore(
        files
    )

    return {
        "message": "Repository processed successfully",
        "files_loaded": len(files)
    }