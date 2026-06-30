import tkinter as tk
import os
from tkinter import filedialog, messagebox
from src.config.settings import BG_COLOR, BUTTON_COLOR, FONT_NAME, ENCRYPTED_FOLDER, KEYS_FOLDER

class EncryptPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_COLOR)
        self.selected_file = None
        self._create_widgets()

    def _create_widgets(self):
        tk.Label(self, text='File Encryption',
                 font=(FONT_NAME, 16, 'bold'),
                 fg='#333333', bg=BG_COLOR).pack(pady=20)

        tk.Button(self, text='Select File', command=self._select_file,
                 bg=BUTTON_COLOR, fg='white', font=(FONT_NAME, 11),
                 relief=tk.FLAT, bd=0, padx=20, pady=8).pack(pady=10)

        self.file_label = tk.Label(self, text='No file selected',
                                    font=(FONT_NAME, 10),
                                    fg='#666666', bg=BG_COLOR)
        self.file_label.pack(pady=5)

        tk.Button(self, text='Encrypt', command=self._encrypt,
                 bg=BUTTON_COLOR, fg='white', font=(FONT_NAME, 11),
                 relief=tk.FLAT, bd=0, padx=20, pady=8).pack(pady=20)

        self.status_label = tk.Label(self, text='',
                                      font=(FONT_NAME, 10),
                                      fg='#333333', bg=BG_COLOR)
        self.status_label.pack(pady=5)

    def _select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.selected_file = file_path
            self.file_label.configure(text=f'Selected: {os.path.basename(file_path)}')

    def _encrypt(self):
        if not self.selected_file:
            messagebox.showwarning('Warning', 'Please select a file first')
            return
        from src.utils.sm4_utils import encrypt_file
        try:
            key = os.urandom(16)
            output_path = os.path.join(ENCRYPTED_FOLDER, os.path.basename(self.selected_file) + '.enc')
            success = encrypt_file(key, self.selected_file, output_path)
            if success:
                key_path = os.path.join(KEYS_FOLDER, os.path.basename(self.selected_file) + '.key')
                with open(key_path, 'wb') as f:
                    f.write(key)
                self.status_label.configure(text='Encryption successful!', fg='green')
                messagebox.showinfo('Success', f'File encrypted!\nKey saved to: {key_path}')
            else:
                self.status_label.configure(text='Encryption failed', fg='red')
        except Exception as e:
            self.status_label.configure(text=f'Error: {str(e)}', fg='red')
