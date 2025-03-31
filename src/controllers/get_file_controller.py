from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from src.services.s3_service import S3Service

router = APIRouter()

# Initialize S3 service
s3_service = S3Service()

@router.get("/{filename}", response_description="File content retrieved successfully")
async def get_file_content(filename: str):
    """
    Retrieve the content of a specified file from the S3 bucket.

    - **filename**: The name of the file to retrieve
    """
    try:
        # Get file content from S3
        file_content = s3_service.download_file(filename)
        return StreamingResponse(file_content, media_type="application/octet-stream")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve file content: {str(e)}")
