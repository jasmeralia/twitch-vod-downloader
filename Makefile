PYTHON ?= .venv/bin/python
PIP ?= $(PYTHON) -m pip

.PHONY: venv install lintfix lint clean

venv:
	python3 -m venv .venv

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements-dev.txt

lintfix: install
	$(PYTHON) -m ruff check --fix twitch_vod_downloader.py settings.py
	$(PYTHON) -m ruff format twitch_vod_downloader.py settings.py

lint: install
	$(PYTHON) -m ruff check twitch_vod_downloader.py settings.py
	$(PYTHON) -m mypy twitch_vod_downloader.py settings.py

clean:
	rm -rf .venv .mypy_cache .ruff_cache
