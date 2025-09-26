🧠 QA API — Вопросы и Ответы
RESTful API для управления вопросами и ответами, построенное на FastAPI, PostgreSQL, SQLAlchemy ORM и Alembic.
Поддерживает асинхронную работу, автоматическую документацию и легко разворачивается через Docker Compose.

🚀 Функционал
✅ Создание, чтение, обновление и удаление вопросов
✅ Создание, чтение, обновление и удаление ответов
✅ Каскадное удаление: при удалении вопроса удаляются все связанные ответы
✅ Валидация данных через Pydantic
✅ Автоматическая документация: Swagger UI и ReDoc
✅ Миграции базы данных через Alembic
✅ Полная изоляция через Docker и Docker Compose
🛠️ Технологии
Backend: FastAPI
База данных: PostgreSQL
ORM: SQLAlchemy (асинхронный режим)
Миграции: Alembic
Контейнеризация: Docker + Docker Compose
Драйверы: asyncpg (для FastAPI), psycopg2-binary (для Alembic)
📦 Установка и запуск
git clone https://github.com/22Zamir/TEST_API.git
cd TEST_API

2. Запустите приложение с помощью Docker Compose
   docker-compose up --build
3. После запуска откройте в браузере:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

Локальная разработка (без Docker)
Создайте виртуальное окружение:
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\Activate.ps1 # Windows
Установите зависимости
pip install -r requirements.txt
Создайте файл .env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/qa_db
Запустите PostgreSQL (например, через Docker)
docker run --name qa-postgres \
-e POSTGRES_DB=qa_db \
-e POSTGRES_USER=user \
-e POSTGRES_PASSWORD=password \
-p 5432:5432 \
-d postgres:15
Примените миграции:
alembic upgrade head
Запустите сервер:
uvicorn app.main:app --reload