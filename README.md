# People API

**Author**: Joseph Hangarter
**Version**: 1.0.4

## Overview
* Features - Django REST Framework
    * Make your site a DRF powered API as you did in previous lab.
    * Adjust project’s permissions so that only authenticated user’s have access to API.
    * Add a custom permission so that only author of blog post can update or delete it.
    * Add ability to switch user’s directly from browsable API.
* Features - Docker
    * create Dockerfile based off python:3.7-slim
    * create docker-compose.yml to run Django app as a web service.
    * enter docker-compose up --build to start your site.
    * add postgres 11 as a service
    * include a volume so that data can persist when container is shut down.
    * Go to browsable api and confirm site properly restricts users based on their permissions.


## Getting Started
* run `pipenv shell`
* install django
* install docker
* install docker-compose
* docker-compose run web ./manage.py runserver

## Routes
* admin page- `http://127.0.0.1:8000/admin`; admin page
* person list - `http://localhost:8000/api/v1/person/`
* person details `<pk>` - `http://localhost:8000/api/v1/person/1/`

## Architecture
* `django`
* `djangorestframework`
* `docker`
* `docker-compose`
* `psycopg2-binary`

