### BASE - Using ubuntu LTS version
FROM ubuntu:20.04 AS base

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install --no-install-recommends -y \
   vim python3.8 python3.8-dev python3.8-venv python3-pip \
   python3-wheel libpq-dev build-essential libssl-dev libffi-dev && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

# install requirements
COPY requirements.txt .

RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /app
EXPOSE 5000

ARG GIT_HASH
ENV GIT_HASH=${GIT_HASH:-dev}



### DEV
FROM base AS development

COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip3 install --no-cache-dir -r requirements-dev.txt

COPY . /app

CMD ["flask", "run", "--reload", "--debugger", "--host", "0.0.0.0"]



### PROD
FROM base AS production

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

COPY . /app

CMD ["uwsgi", "--ini", "uwsgi.ini"]
