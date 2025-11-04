# Use slim Python base for smaller image size
FROM python:3.14-slim

# Install system dependencies (add sqlite3 here)
RUN apt-get update && apt-get install -y --no-install-recommends \
    sqlite3 \
    inotify-tools \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.9.5 /uv /uvx /bin/

# Avoid .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /livex

# Copy pyproject.toml and uv.lock first (for caching deps)
COPY pyproject.toml /livex/
COPY uv.lock /livex/

# Sync dependencies with uv
RUN uv sync --locked

# Copy project files
COPY . /livex/