from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from src.services.s3_service import S3Service

router = APIRouter()

# Initialize S3 service
s3_service = S3Service()

@router.get("/", response_description="List of files retrieved successfully")
async def list_files():
    """
    Retrieve a list of all files stored in the S3 bucket.
    """
    try:
        # List files from S3
        files = s3_service.list_files()
        return JSONResponse(status_code=200, content={"files": files})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list files: {str(e)}")
