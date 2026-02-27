# Todo App — Fullstack Application

A web-based task management application with user registration, authentication, and full CRUD functionality.

## Technology Stack

**Backend:**
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Docker

**Frontend:**
- Next.js 14
- React
- Tailwind CSS
- Axios

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Git

### Setup

1. **Clone the repository and navigate to the project directory:**
```bash
cd todo-app
```

2. **Create a `.env` file in the project root:**

Refer to `.env.example` for the required variables.

3. **Build and start the application:**
```bash
docker-compose up --build
```

4. **Run database migrations (in a separate terminal):**
```bash
docker-compose exec backend python manage.py migrate
```

5. **Create a superuser (optional):**
```bash
docker-compose exec backend python manage.py createsuperuser
```

## Access

| Service | URL |
|---|---|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000/api |
| Django Admin | http://localhost:8000/admin |

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Obtain access token |
| POST | `/api/auth/refresh/` | Refresh access token |

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/tasks/` | List all tasks |
| POST | `/api/tasks/` | Create a task |
| GET | `/api/tasks/{id}/` | Retrieve a task |
| PUT | `/api/tasks/{id}/` | Update a task |
| DELETE | `/api/tasks/{id}/` | Delete a task |

## Features

- User registration and authentication
- JWT-based authorization
- Full CRUD operations for tasks
- Task filtering by status
- Sorting by creation date
- Responsive design
- Input validation
- Error handling
- Docker containerization

## Development

### Stop containers
```bash
docker-compose down
```

### Restart a specific service
```bash
docker-compose restart backend
docker-compose restart frontend
```

### View logs
```bash
docker-compose logs backend
docker-compose logs frontend
```

### Run Django management commands
```bash
docker-compose exec backend python manage.py shell
docker-compose exec backend python manage.py makemigrations
```

## API Testing

### Register
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123"}'
```

### Login
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### Create a task
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{"title": "My task", "description": "Task description"}'
```

## Troubleshooting

### Ports already in use

If ports 3000 or 8000 are occupied, update the port mappings in `docker-compose.yml`.

### Permission issues
```bash
sudo chown -R $USER:$USER .
```

### Docker cleanup
```bash
docker-compose down -v
docker system prune -a
```
