FROM python:3.11-bullseye AS base

ARG APP_UID=5555
ARG APP_GID=5555

ENV POETRY_VERSION=1.5.1

RUN apt-get update && \
    pip install --upgrade pip setuptools && \
    pip install poetry==$POETRY_VERSION && \
    groupadd -r --gid ${APP_GID} app && \
    useradd -r -l -m -s /bin/false -g app --uid ${APP_UID} app && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /template_fastapi
WORKDIR /template_fastapi

COPY --chown=app:app pyproject.toml poetry.lock ./
COPY --chown=app:app src src

RUN poetry config --local virtualenvs.create false && \
    poetry install --only main

ENV PROJECT_API_API_HOST="0.0.0.0"

FROM base AS prod
USER app
ENTRYPOINT ["python3", "src/project_api/main.py"]

FROM base AS dev
RUN apt-get install -y git && \
    poetry install

COPY .git ./.git
COPY .pre-commit-config.yaml ./.pre-commit-config.yaml
RUN pre-commit

CMD ["python3", "src/project_api/main.py"]
