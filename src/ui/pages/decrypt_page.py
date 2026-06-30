import tkinter as tk
from src.ui.pages.decrypt_page.decrypt_page import DecryptPage as DecryptPageImpl

class DecryptPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.impl = DecryptPageImpl(self)
        self.impl.pack(fill=tk.BOTH, expand=True)
