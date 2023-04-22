FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.11

# Install Poetry
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry

# Set up the working directory
WORKDIR /app