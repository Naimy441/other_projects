import keyboard, mouse, random

keyboard.remap_key('m', 'n')
keyboard.remap_key('n', 'm')

keyboard.remap_hotkey('shift+i', 'l')
keyboard.remap_hotkey('l', 'shift+i')

def random_keyboard_error(event):
    if random.randint(1, 6) != 1:
        keyboard.send(event.name)

for key in ['backspace', 'space', 'enter']:
    keyboard.on_press_key(key, random_keyboard_error, suppress=True)

def random_mouse_error():
    if random.randint(1, 16) == 1:
        mouse.click(button='right')

mouse.on_click(random_mouse_error)
