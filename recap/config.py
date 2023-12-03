from pydantic_settings import BaseSettings


class Config(BaseSettings):
    github_user: str
    github_pat_token: str
