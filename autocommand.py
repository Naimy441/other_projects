import debug, keyboard
debug.config(True, 'autocommand.bat')
debug.pause(True)
debug.minimize_batch_windows()

def mouseinfo():
    keyboard.send('windows')
    debug.sleep(0.4)
    keyboard.write('python')
    debug.sleep(0.1)
    keyboard.send('enter')
    debug.sleep(1.5)
    keyboard.write('import pyautogui; pyautogui.mouseInfo()')
    keyboard.send('enter')


def setup():
    keyboard.write('import debug \ndebug.config(True, \'batch_file_name.bat\')\ndebug.pause(True) \ndebug.minimize_batch_window()')


commands = {
    '\\mouseinfo' : mouseinfo,
    '\\setup' : setup
}

for command, function in commands.items():
    def wrapped_function():
        keyboard.send('ctrl+backspace')
        keyboard.send('backspace')
        function()

    keyboard.add_word_listener(command, wrapped_function, timeout=8)

keyboard.wait('shift+escape')
print('Program Completed.')
