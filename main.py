import pyautogui
from pynput import mouse

s = []  # Список для координат мыши
# Обработка нажатий
def on_click(x, y, button, pressed):
    if pressed:
        s.append(x)
        s.append(y)
        x_1 = x
        y_1 = y
        pressed_status = 'on'
        print(f"Позиция курсора: x: {x_1}, y: {y_1} | Статус нажатия: {pressed_status} | Кнопка: {button}")
    else:
        s.append(x)
        s.append(y)
        x_2 = x
        y_2 = y
        pressed_status = 'off'
        print(f"Позиция курсора: x: {x_2}, y: {y_2} | Статус нажатия: {pressed_status} | Кнопка: {button}")
        return False


# Собираем события пока не закончится поток
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# Запускаем метод для отслеживания мыши
listener = mouse.Listener(on_click=on_click)
listener.start()
x_1 = s[0]
y_1 = s[1]

x_2 = s[2]
y_2 = s[3]

print(f"Позиция курсора 1: x: {x_1}, y: {y_1}")
print(f"Позиция курсора 2: x: {x_2}, y: {y_2}")

screenshot = pyautogui.screenshot('screenshot.png', region=(x_1, y_1, x_2, y_2))  # Скрин области
