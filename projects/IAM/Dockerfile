FROM python:3.9.9-bullseye
LABEL org.opencontainers.image.authors="hi@kaiobrito.com"

# set env variables
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	LC_ALL=C.UTF-8 \
	LANG=C.UTF-8 \
	TZ=America/Vancouver

WORKDIR /app

# install system packages
RUN pip install poetry
COPY projects/IAM/poetry.lock projects/IAM/pyproject.toml /app/
RUN poetry config virtualenvs.create false \
        && poetry install --no-interaction --no-ansi


RUN  adduser -u 5678 --disabled-password --gecos "" appuser \
	&& chown -R appuser .

USER appuser

COPY projects/IAM/	.

COPY ./common/logging ./utils/logging


ARG SECRET_KEY=secret

RUN ./manage.py collectstatic --no-input

EXPOSE 8000

CMD [ "gunicorn",  "IAM.asgi:application", "-k", "uvicorn.workers.UvicornWorker" ]
