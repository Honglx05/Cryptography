
import os


def dich_hash(s: str) -> str:
    """Chuẩn hóa chuỗi mã băm: bỏ khoảng trắng và chuyển thành chữ thường."""
    if s is None:
        return ''
    return ''.join(s.split()).lower()


def so_sanhhash(local_hash: str, server_hash: str):
    """
    So sánh 2 mã băm (không phân biệt chữ hoa chữ thường, bỏ khoảng trắng).
    Trả về (boolean, message)
    """
    lh = dich_hash(local_hash)
    sh = dich_hash(server_hash)
    if not lh:
        return False, 'Local hash rỗng.'
    if not sh:
        return False, 'Server hash rỗng.'
    if lh == sh:
        return True, ' File toàn vẹn'
    else:
        return False, 'File không toàn vẹn.'
    print(f"[DEBUG] Local: {lh}")
    print(f"[DEBUG] Server: {sh}")



def doc_hash(filepath: str) -> str:
    """
    Đọc chuỗi checksum từ file (nếu server cung cấp dưới dạng file .txt).
    Lấy dòng đầu tiên có chứa hex.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                return line
    return ''
