import tkinter as tk
from tkinter import RIGHT, N

from PIL import ImageTk
from PIL.Image import Image


win1 = tk.Tk()  # Создал окно
win0 = tk.Tk()  # Создал окно
win0.attributes('-fullscreen', True)  # Полноэкранный режим окна
win0.attributes("-alpha", 0.01)  # прозрачность
win1.attributes("-topmost", True)  # Всегда по верх других окон
win1.title('Толмач')


win1.geometry('300x300+100+200')

def close():  # Закрывает оба окна
    win0.destroy()
    win1.destroy()



close = tk.Button(win1, text='Закрыть', command=close)
close.pack(side=RIGHT, anchor=N)

def screen():
    print('Скрин')

translit = tk.Button(win1, text='Перевести', command=screen)
translit.pack(side=RIGHT, anchor=N)


#win0.configure(background = image1)
win1.mainloop()
win0.mainloop()
