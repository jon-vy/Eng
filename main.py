import pyautogui
from pynput import keyboard
import open_win

def on_release(key):
    if key == keyboard.Key.print_screen:
        open_win.window()
        #screen_zone.screen()
        return False  # Остановить слушатель



with keyboard.Listener(on_release=on_release) as listener:
    listener.join()


listener = keyboard.Listener(on_release=on_release)
listener.start()

