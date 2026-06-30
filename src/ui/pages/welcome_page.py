import tkinter as tk
from src.config.settings import BG_COLOR, ACCENT_COLOR, FONT_NAME

class WelcomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_COLOR)
        self._create_widgets()

    def _create_widgets(self):
        tk.Label(self, text='SM4 Encryption Tool',
                 font=(FONT_NAME, 24, 'bold'),
                 fg=ACCENT_COLOR, bg=BG_COLOR).pack(pady=(80, 20))
        tk.Label(self, text='National Standard SM4 File Encryption/Decryption',
                 font=(FONT_NAME, 12),
                 fg='#666666', bg=BG_COLOR).pack(pady=10)
        tk.Label(self, text='GB/T 32907-2016',
                 font=(FONT_NAME, 10),
                 fg='#999999', bg=BG_COLOR).pack(pady=5)
