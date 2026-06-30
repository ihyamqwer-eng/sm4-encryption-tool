import tkinter as tk
from src.config.settings import NAV_BG, NAV_ACTIVE, TEXT_COLOR, BUTTON_COLOR, ACCENT_COLOR, FONT_NAME

class Navbar(tk.Frame):
    def __init__(self, parent, on_page_change):
        super().__init__(parent, bg=NAV_BG, width=180)
        self.on_page_change = on_page_change
        self.buttons = {}
        self._create_nav_buttons()

    def _create_nav_buttons(self):
        tk.Label(self, text='SM4 Tool', bg=NAV_BG, fg=ACCENT_COLOR,
                 font=(FONT_NAME, 14, 'bold')).pack(pady=(20, 30))

        items = [
            ('welcome', 'Home'),
            ('encrypt', 'Encrypt'),
            ('decrypt', 'Decrypt'),
            ('transfer', 'Transfer'),
            ('tools', 'Tools'),
        ]
        for key, label in items:
            btn = tk.Button(self, text=label, bg=BUTTON_COLOR, fg='white',
                           font=(FONT_NAME, 11), relief=tk.FLAT, bd=0,
                           padx=20, pady=10, cursor='hand2')
            btn.configure(command=lambda k=key: self._on_click(k, btn))
            btn.pack(fill=tk.X, padx=15, pady=5)
            self.buttons[key] = btn

    def _on_click(self, key, btn):
        for b in self.buttons.values():
            b.configure(bg=BUTTON_COLOR)
        btn.configure(bg=ACCENT_COLOR)
        self.on_page_change(key)
