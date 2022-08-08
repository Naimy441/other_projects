import pyautogui
import keyboard

def get_current_windows():
    windows = []
    for window in pyautogui.getAllWindows():
        if not window.title in ['', 'Program Manager', 'Alienware Command Center', 'Windows Input Experience', 'Settings', r'C:\WINDOWS\system32\cmd.exe']:
            windows.append(window)
    
    return windows


def create_keymap():
    accepted_answers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    keymap = {}
    for index, window in enumerate(get_current_windows()):
        answer = input(f'{window.title} --> ')
        if answer in accepted_answers:
            keymap[answer] = window

    return keymap


def maximize_binded_window(event):
    global keymap
    
    numeric_scan_codes = {79: '1', 80: '2', 81: '3', 75: '4', 76: '5', 77: '6', 71: '7', 72: '8', 73: '9'}
    if event.scan_code in list(numeric_scan_codes.keys()) and event.name in list(numeric_scan_codes.values()):
        keyboard.send('backspace')
        try:
            for window in keymap.values():
                window.minimize()
            keymap[numeric_scan_codes[event.scan_code]].maximize()
        except:
            print('Error: that numeric key is not binded to any window.')


def edit_keymap():
    global keymap 

    keyboard.send('backspace')
    keymap = create_keymap()


if __name__ == '__main__':
    keymap = create_keymap()
    keyboard.on_press(maximize_binded_window)
    keyboard.add_hotkey(82, edit_keymap)
    keyboard.wait()