import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class S3Service:
    def __init__(self, bucket_name: str = "bucket-for-ai-generated-content"):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name

    def upload_file(self, file_obj, filename: str):
        """
        Uploads a file to the specified S3 bucket.

        :param file_obj: The file object to upload.
        :param filename: The name to assign to the file in the bucket.
        :raises Exception: If the upload fails.
        """
        try:
            self.s3_client.upload_fileobj(file_obj, self.bucket_name, filename)
            logger.info(f"File {filename} uploaded successfully.")
        except NoCredentialsError:
            logger.error("AWS credentials not found.")
            raise Exception("AWS credentials not found.")
        except ClientError as e:
            logger.error(f"Failed to upload file: {str(e)}")
            raise Exception(f"Failed to upload file: {str(e)}")

    def list_files(self) -> List[str]:
        """
        Lists all files in the specified S3 bucket.

        :return: A list of filenames in the bucket.
        :raises Exception: If the list operation fails.
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            files = [content['Key'] for content in response.get('Contents', [])]
            logger.info("Files retrieved successfully.")
            return files
        except ClientError as e:
            logger.error(f"Failed to list files: {str(e)}")
            raise Exception(f"Failed to list files: {str(e)}")

    def download_file(self, filename: str):
        """
        Downloads a file from the specified S3 bucket.

        :param filename: The name of the file to download.
        :return: A file-like object of the downloaded file.
        :raises Exception: If the download fails.
        """
        try:
            file_obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=filename)
            logger.info(f"File {filename} downloaded successfully.")
            return file_obj['Body']
        except ClientError as e:
            logger.error(f"Failed to download file: {str(e)}")
            raise Exception(f"Failed to download file: {str(e)}")
