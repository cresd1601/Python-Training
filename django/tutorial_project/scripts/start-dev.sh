#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python /usr/src/app/src/manage.py migrate

# Start Django development server
echo "Starting Django development server..."
python /usr/src/app/src/manage.py runserver 0.0.0.0:8000