# https://youtu.be/grnchooO2wU
from tkinter import *

class ChildWindow:
    def __init__(self, parent, width, height, title, resizable=(False, False), icon=None):  # Какие параметры передавать
        self.root = Toplevel(parent)  # Дочернее окно
        self.root.title(title)
        self.root.attributes("-topmost", True)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])  # Размеры окна
        if icon:
            self.root.iconbitmap(icon)  # Иконка у окна

        self.grab_focus()  # как только будет создано окно оно заберёт себе фокус

    def grab_focus(self):
        self.root.grab_set()  # Забирает фокус себе
        self.root.focus_set()  # Захватывает фокус
        self.root.wait_window()  # Ждёт пока не будет уничтожено окно забравшее фокус

