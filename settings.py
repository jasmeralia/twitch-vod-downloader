from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "/app/.env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    channels: str = ""
    data_dir: str = "/data"
    vod_real_path: str | None = None
    smtp_host: str | None = None
    smtp_port: int = 587
    smtp_username: str | None = None
    smtp_password: str | None = None
    smtp_from: str | None = None
    smtp_to: str | None = None

    def channel_list(self) -> list[str]:
        return [c.strip() for c in self.channels.split(",") if c.strip()]


settings = Settings()
