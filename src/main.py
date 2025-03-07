from fastapi import FastAPI
from src.controllers import file_controller

app = FastAPI()

app.include_router(file_controller.router)

# You can add more routers here if needed for additional functionality

# Root endpoint for basic health check
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI S3 File Manager"}