import tkinter as tk
import os
from tkinter import filedialog, messagebox
from src.config.settings import BG_COLOR, BUTTON_COLOR, FONT_NAME

class TransferPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_COLOR)
        self._create_widgets()

    def _create_widgets(self):
        tk.Label(self, text='File Transfer',
                 font=(FONT_NAME, 16, 'bold'),
                 fg='#333333', bg=BG_COLOR).pack(pady=20)

        tk.Label(self, text='Select encrypted file to transfer:',
                 font=(FONT_NAME, 10),
                 fg='#666666', bg=BG_COLOR).pack(pady=10)

        tk.Button(self, text='Select File', command=self._select_file,
                 bg=BUTTON_COLOR, fg='white', font=(FONT_NAME, 11),
                 relief=tk.FLAT, bd=0, padx=20, pady=8).pack(pady=10)

        self.file_label = tk.Label(self, text='No file selected',
                                    font=(FONT_NAME, 10),
                                    fg='#666666', bg=BG_COLOR)
        self.file_label.pack(pady=5)

        tk.Button(self, text='Transfer', command=self._transfer,
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

    def _transfer(self):
        self.status_label.configure(text='Transfer feature - implementation pending', fg='blue')
