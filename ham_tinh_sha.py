
import hashlib
import os

CHUNK_SIZE = 4 * 1024 * 1024  


def sha_file(filepath, progress_callback=None):
    h = hashlib.sha256()
    try:
        total = None
        with open(filepath, 'rb') as f:
            try:
                total = os.path.getsize(filepath)
            except Exception:
                total = None

            read = 0
            while True:
                chunk = f.read(CHUNK_SIZE)
                if not chunk:
                    break
                h.update(chunk)
                read += len(chunk)
                if progress_callback and total is not None:
                    progress_callback(read, total)

        return h.hexdigest()

    except Exception as e:
        raise e


def sha_chuoi(text: str) -> str:
    """Tính SHA-256 của một chuỗi text (UTF-8)."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()
