import tkinter as tk

def create_label(parent, text, font=None, fg=None, bg=None):
    label = tk.Label(parent, text=text, font=font or ('Microsoft YaHei', 10),
                     fg=fg or '#333333', bg=bg or '#f0f0f0')
    return label

def create_entry(parent, width=30, show=None):
    entry = tk.Entry(parent, width=width, show=show,
                     font=('Microsoft YaHei', 10), relief=tk.SOLID, bd=1)
    return entry

def create_text_area(parent, width=50, height=10):
    text = tk.Text(parent, width=width, height=height,
                   font=('Microsoft YaHei', 10), relief=tk.SOLID, bd=1)
    return text
