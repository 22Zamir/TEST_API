from fastapi import FastAPI
from .database import Base, engine
from .api import questions, answers

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="QA API",
    description="API for Questions and Answers with FastAPI and PostgreSQL",
    version="1.0.0"
)

app.include_router(questions.router)
app.include_router(answers.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to QA API. Visit /docs for interactive documentation."}
