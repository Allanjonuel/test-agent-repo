import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from typing import List
from fastapi import UploadFile

class S3Service:
    def __init__(self):
        # Initialize the S3 client using default credentials
        self.s3_client = boto3.client('s3')

    def upload_file_to_s3(self, file: UploadFile, bucket_name: str) -> str:
        """
        Upload a file to an S3 bucket.

        :param file: UploadFile - The file to upload
        :param bucket_name: str - The name of the S3 bucket
        :return: str - The location of the uploaded file
        """
        try:
            self.s3_client.upload_fileobj(file.file, bucket_name, file.filename)
            return f"s3://{bucket_name}/{file.filename}"
        except NoCredentialsError:
            raise Exception("Credentials not available")
        except ClientError as e:
            raise Exception(e)

    def list_files_in_s3(self, bucket_name: str) -> List[str]:
        """
        List all files in an S3 bucket.

        :param bucket_name: str - The name of the S3 bucket
        :return: List[str] - A list of file names
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=bucket_name)
            if 'Contents' in response:
                return [item['Key'] for item in response['Contents']]
            return []
        except ClientError as e:
            raise Exception(e)

    def get_file_content_from_s3(self, file_name: str, bucket_name: str) -> str:
        """
        Retrieve the content of a file from an S3 bucket.

        :param file_name: str - The name of the file
        :param bucket_name: str - The name of the S3 bucket
        :return: str - The content of the file
        """
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=file_name)
            content = response['Body'].read().decode('utf-8')
            return content
        except ClientError as e:
            raise Exception(e)