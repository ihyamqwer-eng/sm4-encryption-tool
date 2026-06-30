import tkinter as tk
from tkinter import ttk
from src.ui.navbar import Navbar
from src.ui.pages.welcome_page import WelcomePage
from src.ui.pages.encrypt_page import EncryptPage
from src.ui.pages.decrypt_page import DecryptPage
from src.ui.pages.transfer_page import TransferPage
from src.ui.pages.tools_page import ToolsPage
from src.config.settings import BG_COLOR, WINDOW_TITLE, WINDOW_SIZE

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(True, True)

        self.container = tk.Frame(self.root, bg=BG_COLOR)
        self.container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.navbar = Navbar(self.root, self.show_page)
        self.navbar.pack(side=tk.LEFT, fill=tk.Y)

        self.pages = {}
        self.current_page = None

    def show_page(self, page_name):
        if self.current_page:
            self.current_page.pack_forget()
        if page_name not in self.pages:
            page_class = self._get_page_class(page_name)
            if page_class:
                self.pages[page_name] = page_class(self.container)
        self.current_page = self.pages.get(page_name)
        if self.current_page:
            self.current_page.pack(fill=tk.BOTH, expand=True)

    def _get_page_class(self, name):
        mapping = {
            'welcome': WelcomePage,
            'encrypt': EncryptPage,
            'decrypt': DecryptPage,
            'transfer': TransferPage,
            'tools': ToolsPage,
        }
        return mapping.get(name)

    def run(self):
        self.show_page('welcome')
        self.root.mainloop()


def backend_ui():
    app = MainWindow()
    app.run()
