from backend.github.code_loader import load_python_files

files = load_python_files(
    "uploads/langchain"
)

print("Files:", len(files))

print(files[0]["file"])