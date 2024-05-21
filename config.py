from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_PORT: int = 5432
    DATABASE_URL = "postgresql://postgres:12345@localhost:5432/dbtest04"
    POSTGRES_PASSWORD: str = "12345"
    POSTGRES_USER: str = "postgres"
    POSTGRES_DB: str = "dbtest04"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_HOSTNAME: str = "localhost"
    
    class Config:
        env_file = './.env'


settings = Settings()
settings.DATABASE_PORT: 5432
settings.POSTGRES_PASSWORD: 12345
settings.POSTGRES_USER: "postgres"

