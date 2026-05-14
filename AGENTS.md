# Agent Instructions

This repo downloads Twitch VODs from specified channels using yt-dlp.

## After Any Code Change

```bash
make lint-fix && make lint
```

Resolve all reported issues before committing.

## Git Workflow

- Never push commits directly to `master`. Always open a pull request from a feature/fix branch.
- Use squash merge strategy when merging pull requests.

## Key Files

- `twitch_vod_downloader.py` — main script
- `settings.py` — pydantic-settings configuration (reads `.env` / `/app/.env`)
- `requirements.txt` — runtime dependencies
- `requirements-dev.txt` — lint/type-check tools

## Runtime

- Runs as a Docker container.
- Configure via environment variables or bind-mounted `/app/.env`.
- `CHANNELS` — comma-separated list of Twitch channel names to download.
