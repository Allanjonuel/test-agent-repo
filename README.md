# FastAPI S3 File Manager

## Project Description

The FastAPI S3 File Manager is a web application built with FastAPI to interact with AWS S3 for file management. This application allows users to upload files to an S3 bucket, list all files in the bucket, and retrieve the content of a specific file.

## Features

1. **File Upload**: Users can upload files to the specified S3 bucket.
2. **List Files**: Retrieve and display a list of all files within the bucket.
3. **Get File Content**: Access and return the content of a specified file from the bucket.

## Technical Specifications

- **FastAPI**: Used for building the API endpoints.
- **boto3**: Utilized for AWS S3 interactions.
- **uvicorn**: Employed as the ASGI server to run the application.
- **python-multipart**: Used for handling file uploads.

## Prerequisites

- Python 3.7+
- AWS CLI configured with default credentials to access the S3 bucket.
- An existing S3 bucket named `bucket-for-ai-generated-content`.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/fastapi_s3_file_manager.git
   cd fastapi_s3_file_manager
   ```

2. **Install Dependencies**

   Create and activate a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

   Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   Start the FastAPI application using uvicorn:

   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8005
   ```

   The application will be accessible at `http://0.0.0.0:8005`.

## Usage

- **Upload a File**: Use an HTTP client like Postman or curl to POST a file to `/upload`.
- **List Files**: Send a GET request to `/files` to retrieve a list of all files in the bucket.
- **Get File Content**: Send a GET request to `/files/{filename}` to retrieve the content of a specific file.

## Docker Support

To run the application in a Docker container:

1. **Build the Docker Image**

   ```bash
   docker build -t fastapi-s3-file-manager .
   ```

2. **Run the Docker Container**

   ```bash
   docker run -d -p 8005:8005 fastapi-s3-file-manager
   ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any bug fixes or enhancements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Special thanks to the developers of FastAPI and boto3 for their excellent tools that made this project possible.