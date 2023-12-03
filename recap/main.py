import asyncio

from recap.config import Config
from recap.github_api import GithubAPI


async def main(config: Config) -> None:
    # Get GitHub user activity
    # eg activity in top 5 recent contributed repos
    github_api = GithubAPI(config.github_pat_token)

    activity = await github_api.get_user_activity(config.github_user)
    # Call OpenAI API for top 5 contribs to get a summary
    print(activity)
    # Provide an SVG of the top 5 repos):

    await github_api.close()


if __name__ == "__main__":
    # Get the config
    config = Config()

    asyncio.run(main(config))
