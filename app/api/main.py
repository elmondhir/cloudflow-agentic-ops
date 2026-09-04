from fastapi import FastAPI

from app.config.settings import settings


app = FastAPI(
    title=settings.app_name,
    description="Backend API for the CloudFlow Agentic Operations Copilot.",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": settings.app_name, "environment": settings.app_env}


@app.get("/health")
async def health():
    return {"status": "healthy"}