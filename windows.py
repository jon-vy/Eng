# https://youtu.be/LMsg0poyrHQ
from tkinter import *
from child_window import ChildWindow


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=None):  # Какие параметры передавать
        '''
         self означает что эта переменная класса в котором мы работаем и будет видна только в нём.
        Если просто root то это глобальная переменная созданная вне класса
        '''
        self.root = Tk()  # Корневая переменная.
        self.root.title(title)
        self.root.attributes("-topmost", True)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])  # Размеры окна
        if icon:
            self.root.iconbitmap(icon)  # Иконка у окна

    def run(self):
        self.root.mainloop()

    def create_child(self, width, height, title="Толмач", resizable=(False, False), icon=None):
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":  # Это говорит о том что файл для запуска, а не для импорта
    window = Window(500, 500, "parent window")
    window.create_child(200, 100)


    #window.run()


