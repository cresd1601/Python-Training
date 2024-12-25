# Project Setup Instructions

## Step 1: Access Project Directory

Navigate to the project directory:

```bash
cd /python-training/training/django/tutorial_project
```

## Step 2: Create Environment Variables

### Development Mode

In the `env/.env.dev` file, add the following environment variables:

```bash
# SQL settings
SQL_TYPE='postgres'
SQL_ENGINE='django.db.backends.postgresql'
SQL_DATABASE='postgres_database_dev'
SQL_USER='postgres_user_dev'
SQL_PASSWORD='X?2y%L.CIgC>gC>.'
SQL_HOST='database'
SQL_PORT='5432'

# Django settings
DJANGO_ENVIRONMENT='development'
DJANGO_ADMIN_EMAIL='admin@example.com'
DJANGO_ADMIN_USER='django_admin_dev'
DJANGO_ADMIN_PASSWORD='/NM5,aA2yN1PORh.'
DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'
DJANGO_SECRET_KEY='django-insecure-efw+ujd$0g_=%$es0xb3&y%$%lrai^qq$uwybo%wgje53+h197'

# Postgres settings
POSTGRES_DB=${SQL_DATABASE}
POSTGRES_USER=${SQL_USER}
POSTGRES_PASSWORD=${SQL_PASSWORD}
```

### Production Mode

In the `env/.env` file, add the following environment variables (adjust for production):

```bash
# SQL settings
SQL_TYPE='postgres'
SQL_ENGINE='django.db.backends.postgresql'
SQL_DATABASE='postgres_database_prod'
SQL_USER='postgres_user_prod'
SQL_PASSWORD='secure-production-password'
SQL_HOST='database'
SQL_PORT='5432'

# Django settings
DJANGO_ENVIRONMENT='production'
DJANGO_ADMIN_EMAIL='admin@yourdomain.com'
DJANGO_ADMIN_USER='django_admin_prod'
DJANGO_ADMIN_PASSWORD='secure-production-password'
DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'
DJANGO_SECRET_KEY='your-production-secret-key'

# Postgres settings
POSTGRES_DB=${SQL_DATABASE}
POSTGRES_USER=${SQL_USER}
POSTGRES_PASSWORD=${SQL_PASSWORD}
```

## Step 3: Build and Start Docker Containers

### Development Mode

Build the Docker image and start the containers in development mode:

```bash
docker compose -f docker-compose.dev.yml up --build
```

### Production Mode

Build the Docker image and start the containers in production mode:

```bash
docker compose up --build
```

## Step 4: Access Django Practice & Admin

### Development

Access the practice site:

```
http://localhost:8000/store/
```

Access the admin panel:

```
http://localhost:8000/admin/
```

**Note:** Username & Password are defined in your `.env.dev` file for development.

### Production

Access the practice site:

```
http://yourdomain.com/store/
or
http://localhost:1337/store/
```

Access the admin panel:

```
http://yourdomain.com/admin/
or
http://localhost:1337/admin/
```

**Note:** Username & Password are defined in your `.env` file for production.

## Step 5: View OpenAPI Schema and API Documentation (Development Mode Only)

The OpenAPI schema and API documentation are only accessible in **development mode**.

In **development mode**:

- **URL** for OpenAPI Schema (JSON/YAML): `http://localhost:8000/schema/`
- **URL** for Swagger UI: `http://localhost:8000/schema/swagger-ui/`
- **URL** for ReDoc UI: `http://localhost:8000/schema/redoc/`

These routes are disabled in production mode for security and performance reasons.
