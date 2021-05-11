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


screenshot = pyautogui.screenshot('screenshot.png', region=(s[0], s[1], s[2], s[3]))  # Скрин области
#screenshot = pyautogui.screenshot('screenshot.png', region=(0, 0, 300, 300))  # Скрин области
