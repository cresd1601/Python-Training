#!/bin/sh

# Set PYTHONPATH environment variable
export PYTHONPATH=/home/app/web/src

# Apply database migrations
echo "Applying database migrations..."
python /home/app/web/src/manage.py migrate

# Collect static files
echo "Collecting static files..."
python /home/app/web/src/manage.py collectstatic --noinput

# Start Django production server
echo "Starting Django production server..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000