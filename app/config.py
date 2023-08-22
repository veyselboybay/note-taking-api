from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    db_connection: str
    secret: str
    algorithm: str
    expires_in: int

    model_config = SettingsConfigDict(env_file='.env')

config = Config()

# print(config.model_dump())