import datetime

import twitch_vod_downloader as downloader
from settings import Settings


def test_channel_list_normalizes_values() -> None:
    config = Settings(channels=" alpha, beta ,, ", _env_file=None)

    assert config.channel_list() == ["alpha", "beta"]


def test_parse_vod_id() -> None:
    assert downloader.parse_vod_id("twitch 12345") == "12345"
    assert downloader.parse_vod_id("12345") == "12345"


def test_read_archive_lines(tmp_path) -> None:
    archive = tmp_path / "archive.txt"
    archive.write_text("twitch 1\n\ntwitch 2\n", encoding="utf-8")

    assert downloader.read_archive_lines(archive) == {"twitch 1", "twitch 2"}
    assert downloader.read_archive_lines(tmp_path / "missing.txt") == set()


def test_find_vod_files_ignores_partial_files(tmp_path) -> None:
    (tmp_path / "2026-01-01_123_video.mp4").touch()
    (tmp_path / "2026-01-01_123_video.part").touch()

    assert downloader.find_vod_files(tmp_path, "123") == [
        (tmp_path / "2026-01-01_123_video.mp4").resolve()
    ]


def test_seconds_to_next_run(monkeypatch) -> None:
    class FixedDateTime(datetime.datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2026, 8, 14, 2, 30)

    monkeypatch.setattr(downloader.datetime, "datetime", FixedDateTime)

    assert downloader.seconds_to_next_run() == 1800
