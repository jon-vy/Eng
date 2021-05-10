import requests
import pyautogui
from pynput import mouse

# координаты курсора
def on_move(x, y):
    print(f"Позиция курсора: x: {x}, y: {y}")

# Обработка нажатий
#def on_click(x, y, button, pressed):
# def screen(x, y, button, pressed):
#    pressed_status = 'on' if pressed else 'off'
#    print(f"Позиция курсора: x: {x}, y: {y} | Статус нажатия: {pressed_status} | Кнопка: {button}")


def on_click(x, y, button, pressed):
    #pressed_status = 'on' if pressed else 'off'
    if pressed:
        x_1 = x
        y_1 = y
        pressed_status = 'on'
        print(f"Позиция курсора: x: {x_1}, y: {y_1} | Статус нажатия: {pressed_status} | Кнопка: {button}")
    else:
        x_2 = x
        y_2 = y
        pressed_status = 'off'
        print(f"Позиция курсора: x: {x_2}, y: {y_2} | Статус нажатия: {pressed_status} | Кнопка: {button}")








# Собираем события пока не закончится поток
with mouse.Listener(
        on_move=on_move,
        on_click=on_click) as listener:
    listener.join()

# Запускаем метод для отслеживания мыши
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click)
listener.start()

# print(f"Позиция курсора: x: {x_1}, y: {y_1}")
# print(f"Позиция курсора: x: {x_2}, y: {y_2}")

# screen = pyautogui.screenshot('s.png')  # Скрин всего экрана
# screenshot = pyautogui.screenshot('screenshot.png', region=(0, 0, 300, 400))  # Скрин области
# print(screen)

