import tkinter as tk
from tkinter import RIGHT, N
import pyautogui
from PIL import ImageTk, Image


path = 'img/screenshot.png'
win0 = tk.Tk()  # Создал окно
win0.attributes('-fullscreen', True)  # Полноэкранный режим окна
image = Image.open(path)
width = pyautogui.size()[0]
ratio = (width / float(image.size[0]))
height = int((float(image.size[1]) * float(ratio)))
image = image.resize((width, height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
canvas = tk.Canvas(win0, width=width, height=height)
canvas.pack(side="top", fill="both", expand="no")
canvas.create_image(0, 0, anchor="nw", image=image)


def close():  # Закрывает оба окна
    win0.destroy()
    win1.destroy()


win1 = tk.Tk()  # Создал окно
win1.attributes("-topmost", True)  # Всегда по верх других окон
win1.title('Толмач')
close = tk.Button(win1, text='Закрыть', command=close)
close.pack(side=RIGHT, anchor=N)


win1.mainloop()
win0.mainloop()
