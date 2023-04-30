ARG VARIANT=3.11-bullseye
FROM mcr.microsoft.com/devcontainers/python:0-${VARIANT}

# Install Poetry using Pip
RUN pip install --upgrade pip \
    && pip3 install -U pip poetry \
    # Enable tab completion for bash
    && poetry completions bash >> /home/vscode/.bash_completion \
    # Enable tab completion for Zsh
    && mkdir -p /home/vscode/.zfunc/ \
    && poetry completions zsh > /home/vscode/.zfunc/_poetry \
    && echo "fpath+=~/.zfunc\nautoload -Uz compinit && compinit" >> /home/vscode/.zshrc

COPY pyproject.toml poetry.lock /tmp/poetry/
WORKDIR /tmp/poetry
RUN poetry config virtualenvs.create false \
    && poetry install \
    && rm -rf /tmp/poetry