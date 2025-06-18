# Todo App - Fullstack Application

Простое веб-приложение "Список задач" с регистрацией, аутентификацией и управлением задачами.

## Технологический стек

**Backend:**
- Django REST Framework
- PostgreSQL
- JWT аутентификация
- Docker

**Frontend:**
- Next.js 14
- React
- Tailwind CSS
- Axios для API запросов

## Быстрый запуск

### Предварительные требования

- Docker и Docker Compose
- Git

### Шаги запуска

1. **Клонируйте репозиторий и перейдите в папку:**
```bash
cd todo-app
```

2. **Создайте файл .env в корне проекта:**
Смотри .env.example

3. **Запустите приложение:**
```bash
docker-compose up --build
```

4. **Выполните миграции (в новом терминале):**
```bash
docker-compose exec backend python manage.py migrate
```

5. **Создайте суперпользователя (опционально):**
```bash
docker-compose exec backend python manage.py createsuperuser
```

## Доступ к приложению

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000/api
- **Django Admin:** http://localhost:8000/admin

## API Endpoints

### Аутентификация
- `POST /api/auth/register/` - Регистрация
- `POST /api/auth/login/` - Вход
- `POST /api/auth/refresh/` - Обновление токена

### Задачи
- `GET /api/tasks/` - Список задач
- `POST /api/tasks/` - Создание задачи
- `GET /api/tasks/{id}/` - Получение задачи
- `PUT /api/tasks/{id}/` - Обновление задачи
- `DELETE /api/tasks/{id}/` - Удаление задачи

## Функционал

✅ Регистрация и аутентификация пользователей  
✅ JWT токены для безопасности  
✅ CRUD операции для задач  
✅ Фильтрация задач по статусу  
✅ Сортировка по дате создания  
✅ Адаптивный дизайн  
✅ Валидация данных  
✅ Обработка ошибок  
✅ Docker контейнеризация  

## Разработка

### Остановка контейнеров
```bash
docker-compose down
```

### Перезапуск отдельного сервиса
```bash
docker-compose restart backend
docker-compose restart frontend
```

### Просмотр логов
```bash
docker-compose logs backend
docker-compose logs frontend
```

### Выполнение команд Django
```bash
docker-compose exec backend python manage.py shell
docker-compose exec backend python manage.py makemigrations
```

## Тестирование API

### Регистрация
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123"}'
```

### Логин
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### Создание задачи
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{"title": "Моя задача", "description": "Описание задачи"}'
```

## Возможные проблемы и решения

### Порты заняты
Если порты 3000 или 8000 заняты, измените их в `docker-compose.yml`

### Проблемы с правами доступа
```bash
sudo chown -R $USER:$USER .
```

### Очистка Docker
```bash
docker-compose down -v
docker system prune -a
```