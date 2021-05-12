import tkinter as tk
from tkinter import RIGHT, N
win1 = tk.Tk()  # Создал окно
win0 = tk.Tk()  # Создал окно

win0.attributes('-fullscreen', True)  # Полноэкранный режим окна
win1.geometry('300x300+100+200')


win0.config(bg='#fa23e4')
win1.mainloop()
win0.mainloop()
