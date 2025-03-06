from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse, StreamingResponse
from typing import List
from src.services.s3_service import S3Service
import logging

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the router
router = APIRouter()

# Initialize the S3 service
s3_service = S3Service(bucket_name="bucket-for-ai-generated-content")


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Endpoint to upload a file to the S3 bucket.

    :param file: The file to be uploaded.
    :return: JSON response with success message or error details.
    """
    try:
        s3_service.upload_file(file.file, file.filename)
        return JSONResponse(status_code=200, content={"message": "File uploaded successfully"})
    except Exception as e:
        logger.error(f"Failed to upload file: {e}")
        raise HTTPException(status_code=500, detail="File upload failed")


@router.get("/files", response_model=List[str])
async def list_files():
    """
    Endpoint to list all files in the S3 bucket.

    :return: List of filenames in the S3 bucket.
    """
    try:
        files = s3_service.list_files()
        return files
    except Exception as e:
        logger.error(f"Failed to list files: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve file list")


@router.get("/files/{filename}")
async def get_file_content(filename: str):
    """
    Endpoint to get the content of a specified file from the S3 bucket.

    :param filename: The name of the file to retrieve.
    :return: Streaming response with file content or error details.
    """
    try:
        file_content = s3_service.get_file_content(filename)
        return StreamingResponse(file_content, media_type="application/octet-stream")
    except Exception as e:
        logger.error(f"Failed to get file content for {filename}: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve file content")