# Simple pub sub message queue pattern with fastapi + celery + redis

## Installation
```shell
docker-compose build
```

## How to use

```shell
docker-compose up
```

## Endpoints
- SwaggerUI: http://localhost:8000/docs
- Flower Dashboard: http://localhost:5555

## Routes
- http://localhost:8000/tasks: POST input and return task_id
- http://localhost:8000/tasks/{task_id}: GET task status and result, result expires in 60s