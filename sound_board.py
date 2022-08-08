import playsound
import keyboard
import sys

def say_abdullah(event):
    playsound.playsound("C:/Users/abu/python_data/abdullah.mp3")


keyboard.on_release_key('tab', say_abdullah)
keyboard.wait('ctrl+shift+alt+1')
sys.exit()