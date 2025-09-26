from fastapi import FastAPI
from .database import Base, async_engine  # ← Используем async_engine
from .api import questions, answers

app = FastAPI(
    title="QA API",
    description="API for Questions and Answers with FastAPI and PostgreSQL",
    version="1.0.0"
)

app.include_router(questions.router)
app.include_router(answers.router)

# Создаём таблицы при запуске (только для dev!)
@app.on_event("startup")
async def startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def read_root():
    return {"message": "Welcome to QA API. Visit /docs for interactive documentation."}