import os

from ghapi.all import GhApi, pages

USER: str = "joaopalmeiro"
DEFAULT_ENV_VARIABLE: str = "GITHUB_TOKEN"

if __name__ == "__main__":
    api = GhApi(owner=USER, token=os.environ[DEFAULT_ENV_VARIABLE])

    # 1. Get all repositories.

    # More info:
    # - https://docs.github.com/en/rest/reference/repos#list-repositories-for-the-authenticated-user
    # - https://ghapi.fast.ai/page.html#pages
    # - https://github.com/fastai/ghapi/issues/36#issuecomment-836186371

    # Required for `api.last_page()` to work.
    repos_first_page = api.repos.list_for_authenticated_user(
        visibility="all", affiliation="owner"
    )

    repos = pages(
        api.repos.list_for_authenticated_user,
        api.last_page(),
        visibility="all",
        affiliation="owner",
    ).concat()

    # print(repos)
    print(f"Number of repositories: {len(repos)}")
