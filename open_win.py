import tkinter as tk
from pynput import keyboard
from tkinter import RIGHT, N
import pyautogui
from PIL import ImageTk, Image


def window():
    pyautogui.screenshot('img/screenshot.png')  # Делает скрин всего экрана
    path = 'img/screenshot.png'
    win0 = tk.Tk()  # Создал окно
    win0.attributes('-fullscreen', True)  # Полноэкранный режим окна
    #win0.geometry("500x600+300+200")

    win0.attributes("-topmost", True)  # Всегда по верх других окон
    #win0.after_idle(win0.attributes, '-topmost', False)
    image = Image.open(path)
    width = pyautogui.size()[0]
    ratio = (width / float(image.size[0]))
    height = int((float(image.size[1]) * float(ratio)))
    image = image.resize((width, height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(win0, width=width, height=height)
    canvas.pack(side="top", fill="both", expand="no")
    canvas.create_image(0, 0, anchor="nw", image=image)

    win0.bind("<Escape>", lambda event: win0.destroy())



    win0.mainloop()


window()
