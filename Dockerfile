FROM python:3.12-slim AS prod

## Install poetry
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
ENV PATH=$PATH:/etc/poetry/bin
RUN poetry config virtualenvs.create false

##
ENV PYTHONBUFFERED=1
WORKDIR /app
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry config virtualenvs.in-project true
RUN poetry install --only main --no-root
RUN poetry add uvloop

RUN chgrp -R 0 /app && chmod -R g=u /app

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8002", "--workers", "4", "core.wsgi:application"]
