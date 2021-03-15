#!/bin/bash

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate --noinput

echo "Set up Fixtures"
python manage.py loaddata /app/app/fixtures/sample_data.json

echo "Starting server"
uwsgi --http :8000 --wsgi-file pages/wsgi.py --master --process 4 --threads 2
