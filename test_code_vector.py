from backend.github.code_loader import load_python_files
from backend.github.code_vector_store import create_code_vectorstore

files = load_python_files(
    "uploads/langchain"
)

print("Files Loaded:", len(files))

vectorstore = create_code_vectorstore(files)

print("Vector Store Created Successfully")