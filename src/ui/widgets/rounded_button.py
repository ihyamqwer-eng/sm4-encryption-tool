import tkinter as tk

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command=None, width=120, height=35,
                 radius=15, bg_color='#ff6666', text_color='white',
                 font=('Microsoft YaHei', 10)):
        super().__init__(parent, width=width, height=height,
                         bg='#f0f0f0', highlightthickness=0)
        self.command = command

        self.create_oval(5, 5, width-5, height-5, fill=bg_color, outline='')
        self.create_text(width//2, height//2, text=text, fill=text_color,
                        font=font, tags='text')

        self.tag_bind('text', '<Button-1>', lambda e: self.command() if self.command else None)
