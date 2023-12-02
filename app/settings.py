from pathlib import Path
from tempfile import gettempdir

import pydantic
from yarl import URL

TEMP_DIR = Path(gettempdir())


class Settings(pydantic.BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_pass: str
    db_base: str

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme="postgresql",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_base}",
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
