import tkinter as tk

class ModernButton(tk.Canvas):
    def __init__(self, parent, text, command=None, width=150, height=40,
                 bg_color='#ff6666', hover_color='#cc0000', text_color='white',
                 font=('Microsoft YaHei', 11)):
        super().__init__(parent, width=width, height=height,
                         bg='#f0f0f0', highlightthickness=0)
        self.command = command
        self.bg_color = bg_color
        self.hover_color = hover_color

        self.create_rounded_rect(5, 5, width-5, height-5, 8, fill=bg_color, outline='')
        self.create_text(width//2, height//2, text=text, fill=text_color,
                        font=font, tags='text')

        self.tag_bind('text', '<Button-1>', self._on_click)
        self.tag_bind('text', '<Enter>', self._on_enter)
        self.tag_bind('text', '<Leave>', self._on_leave)

    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        points = []
        for i in range(0, 360, 10):
            import math
            x = x2 - radius + math.cos(math.radians(i)) * radius
            y = y2 - radius + math.sin(math.radians(i)) * radius
            if x1 + radius <= x <= x2 - radius and y1 + radius <= y <= y2 - radius:
                continue
            points.append((x, y))
        self.create_polygon(points, **kwargs)

    def _on_click(self, event):
        if self.command:
            self.command()

    def _on_enter(self, event):
        self.itemconfig(1, fill=self.hover_color)

    def _on_leave(self, event):
        self.itemconfig(1, fill=self.bg_color)
