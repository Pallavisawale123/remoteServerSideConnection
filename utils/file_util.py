import logging
import hashlib
import os


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(threadName)-12s][%(levelname)-5s] %(message)s",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler()
    ]
)

def write_file(filename, filecontent):
    """
    Writes the given filecontent to the specified filename.

    :param filename: Name (or path) of the file to write to
    :param filecontent: The content to write into the file
    :return: True if write succeeds, False otherwise
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(filecontent)
        return True
    except Exception as e:
        import logging
        logging.error("Failed to write to %s: %s", filename, e)
        return False

def get_sha256(filename):
    """
    Computes the SHA-256 hash of the given file.

    :param filename: Path to the file
    :return: SHA-256 hash string in hexadecimal format, or None if error
    """
    try:
        sha256_hash = hashlib.sha256()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception as e:
        import logging
        logging.error("Failed to compute SHA-256 for %s: %s", filename, e)
        return None


def is_file_exists(filename):
    """
    Checks if the specified file exists.

    :param filename: Path to the file
    :return: True if the file exists and is a regular file, False otherwise
    """
    try:
        return os.path.isfile(filename)
    except Exception as e:
        import logging
        logging.error("Error checking file existence: %s", e)
        return False


def delete_file(filename):
    """
    Deletes the specified file.

    :param filename: Path to the file
    :return: True if the file was deleted successfully, False otherwise
    """
    try:
        if os.path.isfile(filename):
            os.remove(filename)
            return True
        else:
            return False  # File does not exist or is not a regular file
    except Exception as e:
        import logging
        logging.error("Failed to delete file %s: %s", filename, e)
        return False
