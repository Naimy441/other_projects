from debug import *
import sys, pyperclip, shelve, webbrowser, random
config(False, '#.bat')

log(sys.argv)

pycommands = ['search', 'define', 'copy', 'save', 'list', 'delete', 'test', 'encode', 'decode', 'help']
command = sys.argv[1].lower()

if command == 'search':
    pause(True)
    query = ' '.join(sys.argv[2:])
    log(query)

    special_queries = shelve.open(r'C:/Users/abu/python_data/special_queries')
    for k, v in special_queries.items():
        log(k + ' : ' + v)
        if query == k:
            webbrowser.open(v)
            sys.exit()
    special_queries.close()

    for char in query:
        if char == ':':
            print('Error: query cannot include a colon.\n')
            sys.exit()
    webbrowser.open_new_tab(r'https://www.ecosia.org/search?q=' + query)
elif command == 'define':
    pause(False)
    try:
        word = sys.argv[2]
        log(word)
        webbrowser.open_new_tab(r'https://www.google.com/search?q=' + word + ' definition')
    except:
        print('Error: no word entered.')
elif command == 'copy':
    pause(True)
    clipboard = shelve.open(r'C:/Users/abu/python_data/pydata')
    key = ' '.join(sys.argv[2:])
    log(key)
    if key == '':
        print(f'Error: failure to copy \"{key}\". No key entered.\n')
        sys.exit()
    try:
        value = clipboard[key]
        log(value)
        pyperclip.copy(value)
        print(f'\"{value}\" copied to clipboard.')
    except:
        print(f'Error: failure to copy \"{key}\" from clipboard. Key entered incorrectly.')
    clipboard.close()
elif command == 'save':
    pause(True)
    clipboard = shelve.open(r'C:/Users/abu/python_data/pydata')
    key = ' '.join(sys.argv[2:])
    log(key)
    value = pyperclip.paste()
    log(value)
    for k, v in clipboard.items():
        if key == k:
            print(f'That key already exists. Are you sure you want to overwrite \"{v}\" with \"{value}\"?')
            while True:
                answer = input('(y/n): ').lower()
                if answer == 'y':
                    break
                elif answer == 'n':
                    print('Program terminated.')
                    sys.exit()
                else:
                    print('Please enter \"y\" or \"n.\"')
    clipboard[key] = value
    print(f"\"{value}\" saved as \"{key}\" to computer.")
    clipboard.close()
elif command == 'list':
    pause(True)
    print('Clipboard:')
    clipboard = shelve.open(r'C:/Users/abu/python_data/pydata')
    for k, v in clipboard.items():
        print(f'  - {k}: {v}')
    clipboard.close()
elif command == 'delete':
    pause(True)
    data_set = sys.argv[2]
    key = ' '.join(sys.argv[3:])
    log(data_set)
    log(key)

    shelf = shelve.open(r'C:/Users/abu/python_data/' + data_set)
    try:
        print(f'\"{shelf[key]}\" removed from {data_set}.')
        del shelf[key]
    except:
        print(f'Error: failure to delete \"{key}\". Arguments entered incorrectly.')
    shelf.close()
elif command == 'test':
    pause(True)
    print('Everything is working as planned!')
elif command == 'encode':
    pause(True)
    CHARACTERS = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def encrypt(message):
        encrypted_message_key = ''
        for char in message:
            key_char = char
            if char in CHARACTERS:
                key_char = random.choice(CHARACTERS)
            encrypted_message_key += key_char

        encrypted_message = ''
        for index, char in enumerate(message):
            encrypted_char = char
            if char in CHARACTERS:
                encrypted_char = ''
                message_index = CHARACTERS.find(char)
                encrypted_message_key_index = CHARACTERS.find(encrypted_message_key[index])
                encrypted_char = CHARACTERS[message_index - encrypted_message_key_index]
            encrypted_message += encrypted_char

        return [encrypted_message, encrypted_message_key]

    secret_message = pyperclip.paste()
    encryption = encrypt(secret_message)
    while True:
        count = 0
        for char in f'{encryption[0]} {encryption[1]}':
            if char == ' ':
                count += 1
        if count > 1:
            encryption = encrypt(secret_message)
        else:
            break
    pyperclip.copy(f'{encryption[0]} {encryption[1]}')
    print(f'Encrypted Message: {encryption[0]}\nKey: {encryption[1]}')
elif command == 'decode':
    pause(True)
    CHARACTERS = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def decrypt(encryption):
        encrypted_message = encryption.split()[0]
        encrypted_message_key = encryption.split()[1]

        decrypted_message = ''
        for index, char in enumerate(encrypted_message):
            decrypted_char = char
            if char in CHARACTERS:
                decrypted_char = ''
                encrypted_message_index = CHARACTERS.find(char)
                encrypted_message_key_index = CHARACTERS.find(encrypted_message_key[index])
                decrypted_char = CHARACTERS[abs(encrypted_message_index + encrypted_message_key_index)%len(CHARACTERS)]
            decrypted_message += decrypted_char

        return decrypted_message

    decryption = decrypt(pyperclip.paste())
    pyperclip.copy(decryption)
    print(f'Decrypted Message: {decryption}')
elif command == 'help':
    for pycommand in pycommands:
        print(f'  - {pycommand}')
else:
    pause(True)
    print('Error: command entered incorrectly.')

print('\n')
