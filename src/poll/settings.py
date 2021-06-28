from pydantic import BaseSettings  # для конфигурации всех настроек!


class Settings(BaseSettings):  # Параметры конфигураций которыми мы хотим управлять
    server_host: str = '127.0.0.1'
    server_port: int = 8000

    database_url: str = 'sqlite:/// database.sqlite3.db'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)



