# People API

**Author**: Joseph Hangarter
**Version**: 1.0.9

## Overview
* Model
* Permissions
* Authentication
* Token
* Deployment

## Getting Started
* run `pipenv shell`

* Useful terminal commands:
    * `docker-compose run web ./manage.py makemigrations`
    * `docker-compose run web ./manage.py migrate`
    * `docker-compose down`
    * `docker-compose up --build`

* SSH useful commands, and tips for deployment:
    * `ssh root@<ip address>` - to enter SSH in CLI
    * make sure sure to add .env from repo

## Running the App
* In CLI, type `ssh root@64.227.57.230`
* Once in ssh, type `docker-compose up --build`
* When the build is complete, enter one of the `routes` for `Deployed` shown below

## Routes
* Port - `8000`
* Local 
    * admin page- `http://127.0.0.1:8000/admin`; admin page
    * person list - `http://localhost:8000/api/v1/person/`
    * person details `<pk>` - `http://localhost:8000/api/v1/person/1/`

* Deployed - `Digital Ocean`
    * admin page- `http://64.227.57.230:8000/admin/`
    * person list - `http://64.227.57.230:8000/api/v1/person/`
    * person details `<pk>` - `http://64.227.57.230:8000/api/v1/person/1/`


## Architecture
* Dependencies:
    * `Django`
    * `djangorestframework`
    * `djangorestframework-simplejwt` 
    * `psycopg2-binary` 
    * `gunicorn` 
    * `whitenoise` 
    * `django-cors-headers` 
    * `django-environ` 

