#!/bin/bash

#python /code/manage.py migrate

#python /code/manage.py collectstatic --noinput

python /code/manage.py loaddata /code/data/dnd_character/*.json

python /code/manage.py runserver 0.0.0.0:8000

