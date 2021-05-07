import json
from pathlib import Path
from typing import Dict, List, Sequence, Union
from urllib.parse import urlparse

from ghapi.all import GhApi


def read_txt(path: Path) -> List[str]:
    with open(path) as file:
        lines = file.read().splitlines()

    return lines


def parse_urls(urls: Sequence[str]) -> List[Dict[str, str]]:
    repos = []

    for url in urls:
        owner_repo = urlparse(url).path.strip("/").split("/")
        repo_dict = {"owner": owner_repo[0], "repo": owner_repo[1]}

        repos.append(repo_dict)

    return repos


if __name__ == "__main__":
    api = GhApi()

    url_file = Path("urls") / "python_dv.txt"
    output_file = Path("repos") / "python_dv.json"

    urls = read_txt(url_file)
    repos = parse_urls(urls)

    # print(api.repos.get_all_topics)

    repos_and_topics = []
    for repo in repos:
        # More info:
        # - https://docs.github.com/en/rest/reference/repos#get-all-repository-topics
        # - (owner, repo)
        topics = list(api.repos.get_all_topics(**repo, per_page=100)["names"])

        updated_repo: Dict[str, Union[str, List[str]]] = {
            **repo,
            "topics": topics,
        }

        repos_and_topics.append(updated_repo)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(repos_and_topics, file, ensure_ascii=False, indent=2)
