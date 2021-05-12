import tkinter as tk
from tkinter import RIGHT, N

win = tk.Tk()  # Создал окно
#win.attributes('-fullscreen', True)  # Полноэкранный режим окна
win.geometry('300x300+100+200')
closeButton = tk.Button(win, text='Кнопка 1', height=3, width=6)  # Создал кнопку

closeButton.pack(side=RIGHT, anchor=N)

win.config(bg='#fa23e4')
win.mainloop()