from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    AUTH0_DOMAIN: str
    AUTH0_AUDIENCE: str
    FGA_API_URL: str
    FGA_STORE_ID: str
    FGA_MODEL_ID: str
    FGA_CLIENT_ID: str
    FGA_CLIENT_SECRET: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
