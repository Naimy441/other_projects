import threading, webbrowser, subprocess, sys, time, debug, pyautogui
debug.config(True, 'open.bat')

paths = {
    'anki' : 'C:/Program Files/Anki/anki.exe',
    'schoology' : 'https://harmonytx.schoology.com',
    'college_board' : 'https://apclassroom.collegeboard.org/34/home',
    'amsco' : 'https://drive.google.com/drive/folders/1-89lv5RnAnhlotp1ATaTVH0UeJYAg7f3',
    'harmony_portal' : 'https://my.harmonytx.org/ui/applications',
    'schoology_world_history' : 'https://harmonytx.schoology.com/course/5170643610/materials',
    'naimywatermelon_gmail' : 'https://mail.google.com/mail/u/0/#inbox',
    'naimywatermelon_docs' : 'https://docs.google.com/document/u/0/',
    'naimywatermelon_notes' : 'https://keep.google.com/u/0/#home',
    'abna0078_gmail' : 'https://mail.google.com/mail/u/1/#inbox',
    'watch_now_playlist' : 'https://www.youtube.com/playlist?list=PLO9riZK_fUM-ZesfLOhqHcNbO0a4my8iW',
    'hackerrank' : 'https://www.hackerrank.com/dashboard',
    'atbs' : 'https://automatetheboringstuff.com/2e/#toc',
    'atom' : 'C:/Users/abu/AppData/Local/atom/atom.exe',
    'quran' : 'https://quran.com',
    'youtube' : 'https://www.youtube.com',
    'youtube_subscriptions' : 'https://www.youtube.com/feed/subscriptions',
    'discord' : 'discord',
    'iwp' : 'http://inventwithpython.com/beyond',
    'google' : 'https://www.google.com',
    'notes' : 'https://keep.google.com/u/0/#home'
}

keywords = {
    'apwh' : [paths['anki'], paths['schoology_world_history'], paths['college_board'], paths['amsco']],
    'sat' : [],
    'naimy_docs' : [paths['naimywatermelon_docs']],
    'hw' : [paths['harmony_portal'], paths['schoology']],
    'chill' : [paths['watch_now_playlist'], paths['youtube_subscriptions'], paths['discord']],
    'emails' : [paths['naimywatermelon_gmail'], paths['abna0078_gmail']],
    'hackerrank' : [paths['hackerrank']],
    'code' : [paths['atbs'], paths['atom'], paths['iwp']],
    'quran' : [paths['anki'], paths['quran'], paths['youtube']],
    'atom' : [paths['atom']],
    'atbs' : [paths['atbs']],
    'yt_subs' : [paths['youtube_subscriptions']],
    'systemize' : [paths['naimywatermelon_docs'], paths['naimywatermelon_notes']],
    'google' : [paths['google']]
}

def Open(path):
    if 'https://' in path or 'http://' in path:
        print(f'Opening {path} . . .')
        start = time.time()
        webbrowser.open_new_tab(path)
        end = time.time()
        print(f'{path} opened in {round(end-start, 6)} seconds.')
    elif 'C:/' in path:
        print(f'Opening {path} . . .')
        start = time.time()
        subprocess.Popen(path)
        end = time.time()
        print(f'{path} opened in {round(end-start, 6)} seconds.')
    elif path == 'discord':
        print(f'Opening {path} . . .')
        start = time.time()
        pyautogui.press('win')
        pyautogui.write('discord')
        pyautogui.press('enter')
        end = time.time()
        print(f'{path} opened in {round(end-start, 6)} seconds.')
        pyautogui.sleep(2.25)
        if 'Discord' in pyautogui.getActiveWindow().title:
            pyautogui.moveTo(1833, 14)
    else:
        print(f'Error: the path {path} is not a url or process.')

command = sys.argv[1]
if command == 'list':
    debug.pause(True)
    for k in keywords:
        print(f'  -  {k}')
else:
    debug.pause(False)
    for k, v in keywords.items():
        if command == k:
            threads = []
            for path in v:
                thread = threading.Thread(target=Open, args=[path])
                threads.append(thread)
                thread.start()
            break

    for thread in threads:
        thread.join()

print('\nProgram Completed.\n')
