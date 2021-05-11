import pyautogui
from pynput import mouse

s = []  # Список для координат мыши
# Обработка нажатий
def on_click(x, y, button, pressed):
    if pressed:
        s.append(x)
        s.append(y)
    else:
        s.append(x)
        s.append(y)
        return False


# Собираем события пока не закончится поток
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# Запускаем метод для отслеживания мыши
listener = mouse.Listener(on_click=on_click)
listener.start()

x_1 = s[0]  # left
y_1 = s[1]  # top
x_2 = s[2] - s[0]  # width
y_2 = s[3] - s[1]  # height
screenshot = pyautogui.screenshot('screenshot.png', region=(x_1, y_1, x_2, y_2))  # Скрин области
