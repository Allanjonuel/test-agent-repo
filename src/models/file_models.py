from pydantic import BaseModel
from typing import List

class FileUploadResponse(BaseModel):
    file_name: str
    status: str

class FileListResponse(BaseModel):
    files: List[str]