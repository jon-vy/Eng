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

if (s[2] > s[0]):
    left = s[0]
else:
    left = s[2]
if (s[3] > s[1]):
    top = s[1]
else:
    top = s[3]
width = s[2] - s[0]
height = s[3] - s[1]
screenshot = pyautogui.screenshot('screenshot.png', region=(left, top, abs(width), abs(height)))  # Скрин области
