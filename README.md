# Task Manager API

Task Manager API is a Django-based project for managing tasks  
with asynchronous processing using Celery, RabbitMQ, and Elasticsearch  
for search functionality. The project is containerized using Docker  
and monitored with Flower for Celery tasks. The API is built using  
Django REST Framework (DRF).

## Features

- CRUD operations for tasks
- Asynchronous task processing with Celery
- Task status monitoring with Flower
- Full-text search for tasks using Elasticsearch
- Containerized with Docker for easy setup and deployment
- Swagger documentation for API
- Logging for debugging and monitoring

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MBakushin/tms.git
   cd tsm
   
2. Create .env file with:

SECRET_KEY=@zqv@=1#1kkz8nvjzatdr^m0y=#41^dq*khu5@6_&*x=)c!ea5  
POSTGRES_DB=postgres  
POSTGRES_USER=postgres  
POSTGRES_PASSWORD=postgres  
DB_PORT=5432  
DB_HOST=db  
DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres  
CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672/  
CELERY_RESULT_BACKEND=rpc://  
RABBITMQ_DEFAULT_USER=guest  
RABBITMQ_DEFAULT_PASS=guest 

  or you can generate django secret key with 

django-admin shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

  and add value for other parameters

3. Create volume for postgres:

mkdir postgres_data

4. Build and start the containers:

docker-compose up --build

Apply database migrations:

docker-compose exec drf python manage.py migrate

Create a superuser to access the Django admin:

docker-compose exec drf python manage.py createsuperuser

### API Endpoints
The API is available at http://localhost:8000/api/.

List all tasks

GET /api/tasks/

Create a new task

POST /api/tasks/
{
    "title": "New Task",
    "description": "New Description"
}

Retrieve a task

GET /api/tasks/{id}/

Update a task

PUT /api/tasks/{id}/
{
    "title": "Updated Task",
    "description": "Updated Description",
    "status": "completed"
}

Delete a task

DELETE /api/tasks/{id}/

Search Tasks
Search tasks by title and description using Elasticsearch.

GET /api/tasks/search/?q={search_query}

Monitoring Celery Tasks
Flower is available at http://localhost:5555/ for monitoring Celery tasks.

Logging
Logging is configured to output to the console. You can view the logs using:

docker-compose logs drf

Swagger Documentation
Swagger documentation is available at http://localhost:8000/docs/.
