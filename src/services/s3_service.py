import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import logging
from typing import List, BinaryIO

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class S3Service:
    def __init__(self, bucket_name: str):
        """
        Initialize the S3Service with the specified S3 bucket name.

        :param bucket_name: Name of the S3 bucket to interact with.
        """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')

    def upload_file(self, file_obj: BinaryIO, filename: str) -> None:
        """
        Upload a file to the S3 bucket.

        :param file_obj: The file object to upload.
        :param filename: The name of the file in S3.
        :raises: Exception if file upload fails.
        """
        try:
            self.s3_client.upload_fileobj(file_obj, self.bucket_name, filename)
            logger.info(f"File {filename} uploaded successfully.")
        except (NoCredentialsError, ClientError) as e:
            logger.error(f"Failed to upload file {filename}: {e}")
            raise Exception("File upload failed")

    def list_files(self) -> List[str]:
        """
        List all files in the S3 bucket.

        :return: A list of filenames in the S3 bucket.
        :raises: Exception if listing files fails.
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' in response:
                file_list = [item['Key'] for item in response['Contents']]
                logger.info("Files retrieved successfully.")
                return file_list
            else:
                return []
        except ClientError as e:
            logger.error(f"Failed to list files: {e}")
            raise Exception("Failed to retrieve file list")

    def get_file_content(self, filename: str) -> BinaryIO:
        """
        Retrieve the content of a specified file from the S3 bucket.

        :param filename: The name of the file to retrieve.
        :return: The file content as a stream.
        :raises: Exception if file retrieval fails.
        """
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=filename)
            logger.info(f"File content for {filename} retrieved successfully.")
            return response['Body']
        except ClientError as e:
            logger.error(f"Failed to get file content for {filename}: {e}")
            raise Exception("Failed to retrieve file content")
