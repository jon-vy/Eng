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

print(tuple(s))

pyautogui.screenshot('screenshot.png', region=tuple(s))  # Скрин области
#pyautogui.screenshot('screenshot1.png', region=(21, 435, 55, 454))  # Скрин области
