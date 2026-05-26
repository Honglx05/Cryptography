# Minh họa SHA-256 - Kiểm tra tính toàn vẹn tệp tin

Ứng dụng giúp tính toán và kiểm tra mã băm SHA-256 để xác định tệp tin có bị thay đổi, chỉnh sửa hay không. Dự án thuộc môn Mã hóa ứng dụng tại trường Đại học Công Thương TP.HCM (HUIT).

## 🚀 Tính năng chính
* **Chọn tệp:** Hỗ trợ tính toán cho mọi định dạng và kích thước tệp.
* **Tính SHA-256:** Sinh chuỗi băm 64 ký tự Hex từ tệp đầu vào, tự động xuất kết quả ra file `_checksum.txt` cùng thư mục.
* **Kiểm tra toàn vẹn:** Hỗ trợ dán (paste) hoặc load trực tiếp file `.txt` chứa mã băm gốc để so sánh với mã băm hiện tại.

## 💻 Công nghệ
* **Ngôn ngữ:** Python 3.
* **Thư viện:** `tkinter` (Giao diện), `hashlib` (Tính toán băm), `threading` (Xử lý đa luồng tránh đơ UI).

## 📖 Hướng dẫn sử dụng
1. Chạy file `main.py` để khởi động ứng dụng.
2. Nhấn **Chọn file...** để tải lên tệp tin bạn muốn kiểm tra.
3. Nhấn **Tính SHA-256**. 
   * *Lưu ý:* Mã băm sau khi tính xong sẽ hiển thị trên màn hình và tự động được lưu thành một file văn bản (`[tên_file]_checksum.txt`) tại cùng thư mục chứa file gốc.
4. Để kiểm tra tính toàn vẹn của tệp, hãy dán mã băm chuẩn vào ô **Checksum server**, hoặc nhấn **Load checksum từ file** để chọn file `.txt` chứa mã chuẩn.
5. Nhấn **So sánh checksum**. Hệ thống sẽ báo hiệu "File toàn vẹn" (nếu khớp) hoặc "File không toàn vẹn" (nếu tệp đã bị thay đổi).
