FROM python:3.11-slim as dependencies

# Installing default dependencies
RUN python -m pip install -Uq pip poetry

WORKDIR /var/www/web

# Copying project metadata
COPY pyproject.toml poetry.lock ./

# Setting up poetry
RUN poetry config virtualenvs.in-project true

# Installing project dependencies
RUN poetry install --no-dev

FROM python:3.11-slim

WORKDIR /var/www/web

#Setup Virtualenv
ENV VIRTUAL_ENV=/var/www/web/.venv
COPY --from=dependencies $VIRTUAL_ENV  $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#Timezone
RUN apt update && apt install tzdata -y
ENV TZ="America/Sao_Paulo"

# Copying source files
COPY . .

# Run migrations and execute app
ENTRYPOINT gunicorn --workers 4 --worker-class uvicorn.workers.UvicornWorker -e PROJ_ENV=prd --bind 0.0.0.0:8000 --name main_api --log-level=info src.main:app

# Expose app port
EXPOSE 8000
