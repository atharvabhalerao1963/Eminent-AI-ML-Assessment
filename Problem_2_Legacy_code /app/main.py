from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Log Analyzer API",
    description=(
        "Analyze large transaction "
        "log files and detect flagged transactions."
    ),
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Log Analyzer API is running"
    }


app.include_router(router)