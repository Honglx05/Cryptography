import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from ham_tinh_sha import sha_file
from so_sanh import so_sanhhash, doc_hash


class App:
    def __init__(self, root):
        self.root = root
        root.title('Minh họa SHA-256 — Kiểm tra tính toàn vẹn file')
        root.geometry('820x420')

        frm = tk.Frame(root, padx=10, pady=10)
        frm.pack(fill=tk.BOTH, expand=True)

        tk.Button(frm, text='Chọn file...', command=self.chon_file).grid(row=0, column=0, sticky='w')
        self.lbl_filepath = tk.Label(frm, text='(chưa chọn file)', anchor='w')
        self.lbl_filepath.grid(row=0, column=1, sticky='we', padx=8)

        tk.Label(frm, text='SHA-256 (file):').grid(row=1, column=0, sticky='w', pady=(8, 0))
        self.entry_local = tk.Entry(frm, width=90)
        self.entry_local.grid(row=1, column=1, sticky='we', pady=(8, 0))

        tk.Label(frm, text='Checksum server (paste hoặc load file):').grid(row=2, column=0, sticky='w', pady=(8, 0))
        self.entry_server = tk.Entry(frm, width=90)
        self.entry_server.grid(row=2, column=1, sticky='we', pady=(8, 0))
        tk.Button(frm, text='Load checksum từ file', command=self.load_server_hash).grid(row=2, column=2, padx=6)

        self.progress_var = tk.StringVar(value='Đang chờ: ')
        self.lbl_progress = tk.Label(frm, textvariable=self.progress_var)
        self.lbl_progress.grid(row=3, column=1, sticky='w', pady=(8, 0))

        btn_frame = tk.Frame(frm)
        btn_frame.grid(row=4, column=1, sticky='w', pady=12)
        tk.Button(btn_frame, text='Tính SHA-256', command=self.nut_tinh).pack(side=tk.LEFT)
        tk.Button(btn_frame, text='So sánh checksum', command=self.ss).pack(side=tk.LEFT, padx=8)
        tk.Button(btn_frame, text='Sao chép hash', command=self.cop_hash).pack(side=tk.LEFT)

        tk.Label(frm, text='Log / Thông tin:').grid(row=5, column=0, sticky='nw')
        self.log = ScrolledText(frm, height=8)
        self.log.grid(row=5, column=1, columnspan=2, sticky='nsew')

        frm.grid_columnconfigure(1, weight=1)
        frm.grid_rowconfigure(5, weight=1)

        self.filepath = None

    def chon_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.filepath = path
            self.lbl_filepath.config(text=path)

    def load_server_hash(self):
        path = filedialog.askopenfilename(title='Chọn file check')
        if path:
            server_hash = doc_hash(path)
            self.entry_server.delete(0, tk.END)
            self.entry_server.insert(0, server_hash)

    def nut_tinh(self):
        if not self.filepath:
            messagebox.showwarning('Chưa chọn file', 'Vui lòng chọn file để tính SHA-256')
            return
        threading.Thread(target=self.tinh_hash, daemon=True).start()

    def tinh_hash(self):
        self.progress_var.set('Đang tính...')
        ma_hash = sha_file(self.filepath)
        self.entry_local.delete(0, tk.END)
        self.entry_local.insert(0, ma_hash)
        self.log.insert(tk.END, f'Hoàn tất: {ma_hash}\n')
        self.progress_var.set('Hoàn tất!')

        file_dir = os.path.dirname(self.filepath)
        file_name = os.path.basename(self.filepath)
        checksum_path = os.path.join(file_dir, f"{file_name}_checksum.txt")
    
        try:
            with open(checksum_path, "w", encoding="utf-8") as f:
                f.write(ma_hash)
            self.log.insert(tk.END, f"Đã lưu checksum tại: {checksum_path}\n")
        except Exception as e:
            self.log.insert(tk.END, f"Lỗi khi ghi file checksum: {e}\n")


    def ss(self):
        local = self.entry_local.get().strip()
        server = self.entry_server.get().strip()
        if not local or not server:
            messagebox.showwarning('Thiếu dữ liệu', 'Vui lòng tính SHA-256 và nhập checksum server.')
            return
    
        ok, msg = so_sanhhash(local, server)
        if ok:
            messagebox.showinfo('Kết quả', msg)
        else:
            messagebox.showerror('Kết quả', msg)


    def cop_hash(self):
        val = self.entry_local.get()
        if val:
            self.root.clipboard_clear()
            self.root.clipboard_append(val)
            messagebox.showinfo('Sao chép', 'Đã sao chép mã băm .')


def run_app():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    run_app()
