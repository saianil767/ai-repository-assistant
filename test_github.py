from backend.github.repo_loader import clone_repo

path = clone_repo(
    "https://github.com/langchain-ai/langchain"
)

print(path)