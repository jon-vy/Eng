import pyautogui
from pynput import keyboard
import test
import screen_zone

def on_press(key):
    try:
        print(f"Клавиша: {key.char}")
    except AttributeError:
        print(f"Спец. клавиша: {key}")


def on_release(key):
    if key == keyboard.Key.print_screen:
        pyautogui.screenshot('screenshot.png')
        #screen_zone.screen()
        return False  # Остановить слушатель


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

