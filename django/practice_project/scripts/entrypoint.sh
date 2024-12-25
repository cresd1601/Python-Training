#!/bin/sh

# Function to wait for PostgreSQL to be ready
wait_for_database() {
  echo "Waiting for PostgreSQL..."

  while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
    sleep 0.1
  done

  echo "PostgreSQL started"
}

# Check if the database type is PostgreSQL
if [ "$SQL_TYPE" = "postgres" ]; then
  wait_for_database
fi

exec "$@"