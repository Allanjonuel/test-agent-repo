# S3 File Manager

A FastAPI application to manage file operations with AWS S3, including file upload, listing, and retrieval.

## Prerequisites

- Python 3.7+
- AWS CLI configured with default credentials

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd s3_file_manager
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

Run the following command to start the FastAPI application using Uvicorn:

```sh
uvicorn src.main:app --host 0.0.0.0 --port 8005
```

The application will be accessible at `http://0.0.0.0:8005`.

## API Endpoints

### 1. Upload File

- **Endpoint:** `/upload`
- **Method:** `POST`
- **Description:** Upload a file to the S3 bucket.
- **Request Body:** multipart/form-data
  - `file`: The file to be uploaded.
- **Response:**
  - `200 OK`: File uploaded successfully.
  - `500 Internal Server Error`: Failed to upload file.

### 2. List Files

- **Endpoint:** `/files`
- **Method:** `GET`
- **Description:** Retrieve a list of all files stored in the S3 bucket.
- **Response:**
  - `200 OK`: List of files retrieved successfully.
  - `500 Internal Server Error`: Failed to list files.

### 3. Get File Content

- **Endpoint:** `/file/{filename}`
- **Method:** `GET`
- **Description:** Retrieve the content of a specified file from the S3 bucket.
- **Parameters:**
  - `filename`: The name of the file to retrieve.
- **Response:**
  - `200 OK`: File content retrieved successfully.
  - `500 Internal Server Error`: Failed to retrieve file content.

## Error Handling

The API provides appropriate HTTP status codes and error messages to indicate issues with requests. Ensure that the AWS S3 bucket permissions are correctly configured and that the application has access to the bucket.

## Logging

The application uses the Python `logging` module to log important events, including error messages and info messages about the success of operations.

## Security Considerations

- Ensure that the AWS credentials are not hard-coded in the application.
- Use IAM roles for permissions management.

## Future Improvements

- Implement authentication and authorization mechanisms.
- Add CORS and rate limiting for enhanced security.
- Improve error handling and logging mechanisms.

---

This application is designed to be scalable and flexible, allowing easy integration with other services and systems that require file management capabilities with AWS S3.