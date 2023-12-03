import aiohttp


class GithubAPI:
    def __init__(self, pat_token: str) -> None:
        """
        Args:
            pat_token (str): Fine-grained Personal Access Token from GitHub
        """
        self._base_url = "https://api.github.com/graphql"

        self.client = aiohttp.ClientSession(
            headers={"Authorization": f"Bearer {pat_token}"}
        )

    async def close(self):
        await self.client.close()
        self.client = None

    async def get_user_activity(self, username: str) -> dict:
        """
        Args:
            username (str): GitHub username
        Returns:
            dict: JSON response from GitHub GraphQL API
        """
        query = (
            """
        query {
            user(login: "%s") {
                name
                repositories(first: 5, orderBy: {field: UPDATED_AT, direction: DESC}) {
                    nodes {
                        name
                        description
                        url
                        updatedAt
                        primaryLanguage {
                            name
                            color
                        }
                    }
                }
            }
        }
        """
            % username
        )

        async with self.client.post(self._base_url, json={"query": query}) as resp:
            return await resp.json()
