import tkinter as tk
from tkinter import RIGHT, N

from PIL import ImageTk
from PIL.Image import Image


win1 = tk.Tk()  # Создал окно
win0 = tk.Tk()  # Создал окно
win0.attributes('-fullscreen', True)  # Полноэкранный режим окна
win0.attributes("-alpha", 0.01)
win1.attributes("-topmost", True)
win1.title('Толмач')

win1.geometry('300x300+100+200')


#win0.configure(background = image1)
win1.mainloop()
win0.mainloop()
