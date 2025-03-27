from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Core",
    description="This is the core of the AI system",
    version="0.1"
)

app.include_router(router, prefix="/api", tags=["LLM", "API"])
