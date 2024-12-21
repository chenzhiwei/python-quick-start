FROM docker.io/library/python:3.12-slim AS builder

COPY src /app/src
COPY uv.lock /app/uv.lock
COPY LICENSE /app/LICENSE
COPY pyproject.toml /app/pyproject.toml
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/bin/uv

WORKDIR /app
RUN uv sync --frozen --no-cache
RUN rm -rf /app/.pdm-build

FROM docker.io/library/python:3.12-slim

LABEL org.opencontainers.image.authors="zhiwei@youya.org"
LABEL org.opencontainers.image.documentation="https://github.com/chenzhiwei/python-quick-start"

COPY --from=builder /app /app

ENV PATH=$PATH:/app/.venv/bin

CMD ["taishan-cli"]
