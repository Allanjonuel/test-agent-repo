from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from src.services.s3_service import S3Service
from src.models.file_models import FileListResponse, FileUploadResponse
from typing import List

router = APIRouter()

# Initialize the S3 service
s3_service = S3Service()

BUCKET_NAME = "bucket-for-ai-generated-content"

@router.post("/upload", response_model=FileUploadResponse)
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a file to the specified S3 bucket.

    Parameters:
    - file: UploadFile - The file to be uploaded

    Returns:
    - FileUploadResponse: The response containing the file name and status
    """
    try:
        file_location = s3_service.upload_file_to_s3(file, BUCKET_NAME)
        return FileUploadResponse(file_name=file.filename, status="success")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/files", response_model=FileListResponse)
async def list_files():
    """
    List all files stored in the specified S3 bucket.

    Returns:
    - FileListResponse: A list of file names
    """
    try:
        files = s3_service.list_files_in_s3(BUCKET_NAME)
        return FileListResponse(files=files)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/files/{file_name}")
async def get_file_content(file_name: str):
    """
    Retrieve the content of a specified file from the S3 bucket.

    Parameters:
    - file_name: str - The name of the file to retrieve

    Returns:
    - JSONResponse: The content of the file
    """
    try:
        file_content = s3_service.get_file_content_from_s3(file_name, BUCKET_NAME)
        return JSONResponse(content={"content": file_content})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))