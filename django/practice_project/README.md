# News Feed System Project Setup Instructions and Estimation

## Estimation Breakdown

### Total Estimated Hours: **64 hours**

**Start Date**: 10/29/2024 - **End Date**: 11/07/2024

| Task                                                  | Description                                                                                                      | Estimated Hours |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------- |
| **1. User Authentication and Authorization System**   | - Implement registration and login functionality - Secure password handling and JWT token generation             | 4               |
| **2. User Profile Management**                        | - Create user profile model and API endpoints - Implement profile update functionality                           | 4               |
| **3. Pagination for List Endpoints**                  | - Implement pagination in API responses for posts and comments                                                   | 2               |
| **4. Rate Limiting for API Endpoints**                | - Set up rate limiting for all relevant API endpoints                                                            | 2               |
| **5. Error Handling and Logging**                     | - Implement centralized error handling - Set up logging for errors and important events                          | 3               |
| **6. Unit Tests**                                     | - Write unit tests for models, views, and serializers (Apply TDD & coverage over 80%)                            | 10              |
| **7. Input Validation and Sanitization**              | - Implement validation for API inputs to prevent security vulnerabilities                                        | 6               |
| **8. API Documentation**                              | - Create documentation for API endpoints using Swagger or similar tools                                          | 2               |
| **9. Admin Dashboard Functionality**                  | - Implement CRUD operations for users, posts, hashtags, and categories - Create UI for admin dashboard           | 8               |
| **10. Ability to Activate/Deactivate Multiple Posts** | - Implement functionality to bulk activate/deactivate posts                                                      | 4               |
| **11. CRUD Operations for Posts Data**                | - Implement endpoints for creating, reading, updating, and deleting posts                                        | 4               |
| **12. CRUD Operations for User Data**                 | - Implement endpoints for creating, reading, updating, and deleting user data                                    | 4               |
| **13. Ability to Like Posts**                         | - Implement liking functionality for posts                                                                       | 4               |
| **14. Ability to Comment on Posts**                   | - Implement commenting functionality for posts                                                                   | 4               |
| **15. List Posts by Tag**                             | - Implement endpoint to list posts filtered by hashtags                                                          | 3               |
| **16. List Posts Ordered by Number of Comments**      | - Implement endpoint to list posts sorted by comment count                                                       | 3               |
| **17. List Posts Ordered by Number of Likes**         | - Implement endpoint to list posts sorted by like count                                                          | 3               |
| **18. Search Posts by Title**                         | - Implement search functionality for posts by title                                                              | 4               |
| **19. Log Messages to Notification Table**            | - Implement background job to log notifications when posts are commented on or liked                             | 6               |
| **20. Integrate Cache Engine (Redis)**                | - Set up Redis for caching API responses - Implement cache invalidation after specified time                     | 8               |
| **21. Integrate Search Engine (ElasticSearch)**       | - Set up ElasticSearch for indexing and searching posts - Implement search functionality by keyword and distance | 10              |
| **22. Seeding Data for Testing and Load Testing**     | - Use FactoryBoy to create test data for development and testing                                                 | 6               |
| **23. Pub/Sub, Queue, Message Bus Integration**       | - Integrate RabbitMQ/Redis or Kafka for message queuing and pub/sub functionality                                | 4               |

## Project Setup Instructions

### Step 1: Access Project Directory

Navigate to the project directory:

```bash
cd /python-training/training/django/practice_project
```

### Step 2: Create Environment Variables

#### Development Mode

In the `env/.env.dev` file, add the following environment variables:

```bash
# SQL settings
SQL_TYPE='postgres'
SQL_ENGINE='django.db.backends.postgresql'
SQL_DATABASE='postgres_database_dev'
SQL_USER='postgres_user_dev'
SQL_PASSWORD='X?2y%L.CIgC>gC>.'
SQL_HOST='database_dev'
SQL_PORT='5432'

# Django settings
DJANGO_ENVIRONMENT='development'
DJANGO_ADMIN_EMAIL='admin@example.com'
DJANGO_ADMIN_USER='django_admin_dev'
DJANGO_ADMIN_PASSWORD='/NM5,aA2yN1PORh.'
DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'
DJANGO_SECRET_KEY='django-insecure-efw+ujd$0g_=%$es0xb3&y%$%lrai^qq$uwybo%wgje53+h197'

# Redis settings
REDIS_HOST='redis_dev'
REDIS_PORT='6379'
REDIS_BROKER_DB='0'
REDIS_CACHE_DB='1'

# Elasticsearch settings
ELASTICSEARCH_HOST='http://elasticsearch_dev:9200'
```

#### Production Mode

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

# Redis settings
REDIS_HOST='redis'
REDIS_PORT='6379'
REDIS_BROKER_DB='0'
REDIS_CACHE_DB='1'

# Elasticsearch settings
ELASTICSEARCH_HOST='http://elasticsearch:9200'

```

### Step 3: Build and Start Docker Containers

#### Development Mode

Build the Docker image and start the containers in development mode:

```bash
docker compose -f docker-compose.dev.yml up --build
```

#### Production Mode

Build the Docker image and start the containers in production mode:

```bash
docker compose up --build
```

### Step 4: Create a New Index for Elasticsearch

After setting up your Django models and Elasticsearch documents, you need to create a new index in Elasticsearch to ensure that the fields are mapped and indexed correctly.

1. **Access the Docker container** with default access to the `src` directory of container:

```bash
docker exec -it backend_dev /bin/bash -c "cd /usr/src/app/src && exec /bin/bash"
```

2. **Create a new index in Elasticsearch** using the Django management command:

```bash
python manage.py search_index --create
```

### Step 5: Access Django Practice & Admin

#### Development

Access the practice site:

```
http://localhost:8000/api/docs/swagger/
```

Access the admin panel:

```
http://localhost:8000/admin/
```

**Note:** Username & Password are defined in your `.env.dev` file for development.

#### Production

Access the practice site:

```
http://yourdomain.com/api/docs/swagger/
or
http://localhost:1337/api/docs/swagger/
```

Access the admin panel:

```
http://yourdomain.com/admin/
or
http://localhost:1337/admin/
```

**Note:** Username & Password are defined in your `.env` file for production.

### Step 6: View OpenAPI Schema and API Documentation (Development Mode Only)

The OpenAPI schema and API documentation are only accessible in **development mode**.

In **development mode**:

- **URL** for OpenAPI Schema (JSON/YAML): `http://localhost:8000/schema/`
- **URL** for Swagger UI: `http://localhost:8000/schema/swagger-ui/`
- **URL** for ReDoc UI: `http://localhost:8000/schema/redoc/`

These routes are disabled in production mode for security and performance reasons.

### Step 7: Running Unit Tests

To ensure your application behaves as expected, you can run unit tests. Here’s how to do it:

1. **Access the Docker container** with default access to the `src` directory of container:

```bash
docker exec -it backend_dev /bin/bash -c "cd /usr/src/app/src && exec /bin/bash"
```

2. **Run the unit tests** using the Django management command:

```bashs
python manage.py test apps
```

This command will discover and execute all tests defined in the `apps/*/tests` directory.

3. **(Optional) Check Test Coverage:** If you want to measure the coverage of your tests, make sure you have the `coverage` package installed. Then run:

```bash
coverage run manage.py test apps
coverage report
```

This will show you a report on the coverage of your tests.
