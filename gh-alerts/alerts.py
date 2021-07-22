import os

from fastcore.net import HTTP404NotFoundError
from ghapi.all import GhApi, pages

USER: str = "joaopalmeiro"
DEFAULT_ENV_VARIABLE: str = "GITHUB_TOKEN"

ENABLE_SYMBOL: str = "🟢"
DISABLE_SYMBOL: str = "❌"

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

    # 2. Check if vulnerability alerts are enabled.

    enabled = disabled = 0
    for repo in repos:
        # `AttrDict`: `dict` subclass that provides access to keys as attributes.
        # More info: https://fastcore.fast.ai/basics.html#AttrDict
        name = repo.name

        # _404 Not Found_ if repository is not enabled with vulnerability alerts.
        # More info: https://docs.github.com/en/rest/reference/repos#check-if-vulnerability-alerts-are-enabled-for-a-repository
        try:
            api.repos.check_vulnerability_alerts(repo=name)

            print(f"{ENABLE_SYMBOL} {name}\n")
            enabled += 1
        except HTTP404NotFoundError:
            print(f"{DISABLE_SYMBOL} {name}\n")
            disabled += 1

    print(
        f"\nNumber of repositories: {len(repos)}\n"
        f"{ENABLE_SYMBOL} {enabled} w/ vulnerability alerts enabled\n"
        f"{DISABLE_SYMBOL} {disabled} w/ vulnerability alerts disabled"
    )
