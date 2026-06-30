import tkinter as tk
import os
from tkinter import messagebox
from src.config.settings import BG_COLOR, BUTTON_COLOR, FONT_NAME
from src.utils.db_utils import KeyDatabase

class ToolsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_COLOR)
        self.db = KeyDatabase()
        self._create_widgets()

    def _create_widgets(self):
        tk.Label(self, text='Tools',
                 font=(FONT_NAME, 16, 'bold'),
                 fg='#333333', bg=BG_COLOR).pack(pady=20)

        tk.Button(self, text='Manage Keys', command=self._manage_keys,
                 bg=BUTTON_COLOR, fg='white', font=(FONT_NAME, 11),
                 relief=tk.FLAT, bd=0, padx=20, pady=8).pack(pady=10)

        tk.Button(self, text='Generate Random Key', command=self._generate_key,
                 bg=BUTTON_COLOR, fg='white', font=(FONT_NAME, 11),
                 relief=tk.FLAT, bd=0, padx=20, pady=8).pack(pady=10)

    def _manage_keys(self):
        keys = self.db.get_all_keys()
        msg = 'Stored keys:\n\n'
        if not keys:
            msg += 'No keys stored.'
        else:
            for k in keys:
                msg += f'ID: {k[0]} - {k[1]} - {k[2]}\n'
        messagebox.showinfo('Key Management', msg)

    def _generate_key(self):
        import secrets
        key = secrets.token_bytes(16)
        from tkinter import simpledialog
        name = simpledialog.askstring('Key Name', 'Enter a name for this key:')
        if name:
            from src.config.settings import KEYS_FOLDER
            key_path = os.path.join(KEYS_FOLDER, f'{name}.key')
            with open(key_path, 'wb') as f:
                f.write(key)
            messagebox.showinfo('Success', f'Key generated and saved to:\n{key_path}')
