import uuid
from typing import Optional


def generate_unique_file_name(file_name: str) -> str:
    """
    Generate a unique file name using UUID.

    :param file_name: str - The original file name
    :return: str - A unique file name
    """
    unique_id = uuid.uuid4()
    return f"{unique_id}_{file_name}"


def convert_bytes_to_human_readable(num: int) -> str:
    """
    Convert bytes to a human-readable format (e.g., KB, MB, GB).

    :param num: int - The number of bytes
    :return: str - The human-readable string
    """
    step_unit = 1024
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if num < step_unit:
            return f"{num:.2f} {unit}"
        num /= step_unit


def get_file_extension(file_name: str) -> Optional[str]:
    """
    Get the file extension from a file name.

    :param file_name: str - The name of the file
    :return: Optional[str] - The file extension or None if not found
    """
    if '.' in file_name:
        return file_name.rsplit('.', 1)[-1]
    return None