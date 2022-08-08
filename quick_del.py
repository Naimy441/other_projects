import keyboard
import mouse
import time

def quick_del():
    mouse.click()
    time.sleep(0.25)
    keyboard.send('delete')
    time.sleep(0.25)
    keyboard.send('enter')

keyboard.add_hotkey('`', quick_del)
keyboard.wait('esc')