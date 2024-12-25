#!/bin/sh

# Navigate to the 'src' directory
echo "Navigating to the src directory..."
cd /usr/src/app/src || exit 1

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start both Django development server and Celery worker in the background
echo "Starting Django development server and Celery worker..."
python manage.py runserver 0.0.0.0:8000 &
celery -A config worker --loglevel=info
