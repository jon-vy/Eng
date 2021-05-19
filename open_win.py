import tkinter as tk
from pynput import keyboard
from tkinter import RIGHT, N
import pyautogui
from PIL import ImageTk, Image
import screen_zone


def window():
    pyautogui.screenshot('img/screenshot.png')  # Делает скрин всего экрана
    path = 'img/screenshot.png'
    win = tk.Tk()  # Создал окно
    win.attributes('-fullscreen', True)  # Полноэкранный режим окна
    #win0.geometry("500x600+300+200")

    win.attributes("-topmost", True)  # Всегда по верх других окон
    #win.after_idle(win0.attributes, '-topmost', False)
    image = Image.open(path)
    width = pyautogui.size()[0]
    ratio = (width / float(image.size[0]))
    height = int((float(image.size[1]) * float(ratio)))
    image = image.resize((width, height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(win, width=width, height=height)
    canvas.pack(side="top", fill="both", expand="no")
    canvas.create_image(0, 0, anchor="nw", image=image)

    win.bind("<Escape>", lambda event: win.destroy())
    win.bind("<KeyPress-Sys_Req>", screen_zone.screen())  # Должна запускать creen_zone.screen()



    win.mainloop()


#window()
