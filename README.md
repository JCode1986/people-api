# People API

**Author**: Joseph Hangarter
**Version**: 1.0.3

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
* python manage.py runserver
* open server from terminal

## Routes
* admin page- `http://127.0.0.1:8000/admin`; admin page
* people page 1 - `http://127.0.0.1:8000/people/1`; people 1
* people page 2 - `http://127.0.0.1:8000/people/2`; people 2

## Architecture
* `django`
* `djangorestframework`
* `docker`
* `docker-compose`
