import keyboard, pyperclip

events = []
def save_event(event):
   events.append(event)

while True:
    print('\nPress shift+escape to start/stop recording.\n')

    keyboard.wait('shift+escape')
    print('Starting recording...')

    keyboard.hook(save_event)

    keyboard.wait('shift+escape')
    print('Stopping recording...')

    keyboard.unhook_all()

    text = ''.join(list(keyboard.get_typed_strings(events)))
    pyperclip.copy(text)
    print(f'\'{text}\' was copied to clipboard.')

    events = []
