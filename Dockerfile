FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir \
    agentscope \
    fastapi \
    uvicorn \
    asyncpg \
    httpx \
    requests \
    pandas \
    openpyxl \
    jinja2
