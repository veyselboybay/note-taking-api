from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    db_connection: str

    model_config = SettingsConfigDict(env_file='.env')

config = Config()

# print(config.model_dump())