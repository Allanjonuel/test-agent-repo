from fastapi import FastAPI
from src.controllers import file_upload_controller, list_files_controller, get_file_controller

app = FastAPI(title="S3 File Manager")

# Include routers from different controllers
app.include_router(file_upload_controller.router, prefix="/upload", tags=["File Upload"])
app.include_router(list_files_controller.router, prefix="/files", tags=["List Files"])
app.include_router(get_file_controller.router, prefix="/file", tags=["Get File Content"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the S3 File Manager API!"}

# TODO: Add middleware for logging and error handling
# TODO: Add security features like CORS
# TODO: Implement rate limiting for better security and performance