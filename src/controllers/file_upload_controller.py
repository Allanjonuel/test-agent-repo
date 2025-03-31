from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from src.services.s3_service import S3Service

router = APIRouter()

# Initialize S3 service
s3_service = S3Service()

@router.post("/", response_description="File uploaded successfully")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a file to the S3 bucket.

    - **file**: The file to be uploaded
    """
    try:
        # Upload file to S3
        s3_service.upload_file(file.file, file.filename)
        return JSONResponse(status_code=200, content={"message": "File uploaded successfully", "filename": file.filename})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")
