from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_PORT: int = 5432
    DATABASE_URL = "postgresql://postgresuser:U4bbcW0F2xCTKhDiiLgC9J4kTwv2owIy@dpg-cp6b5sol6cac738hr7jg-a:5432/dbtest04_82k1"
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

