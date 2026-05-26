# SHA-256 File Integrity Checker

A Python application that calculates and verifies SHA-256 hashes to help you detect if a file has been modified or corrupted.

## 📖 How to Use

1. Run `main.py` to launch the application.
2. Click **Chọn file...** to select the file you want to check.
3. Click **Tính SHA-256** to generate the hash. 
   * *Note:* The result will be displayed on the screen and automatically saved as a `[filename]_checksum.txt` file in the same directory.
4. To verify file integrity, paste the original hash into the **Checksum server** box, or click **Load checksum từ file** to load it from a `.txt` file.
5. Click **So sánh checksum**. The system will notify you if the file is intact ("File toàn vẹn") or modified ("File không toàn vẹn").
