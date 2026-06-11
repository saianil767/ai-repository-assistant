import os
from git import Repo


def clone_repo(repo_url):

    repo_name = repo_url.split("/")[-1]

    local_path = os.path.join(
        "uploads",
        repo_name
    )

    if not os.path.exists(local_path):

        Repo.clone_from(
            repo_url,
            local_path
        )

    return local_path