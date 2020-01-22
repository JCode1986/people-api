# Python version
FROM python:3.7-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

COPY Pipfile Pipfile.lock /code/

# Install dependencies
RUN pip install pipenv && pipenv install --system

COPY . /code/