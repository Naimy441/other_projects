import pyautogui, debug
debug.config(True, 'auto_dino.bat')
debug.pause(True)
debug.minimize_batch_windows()

while True:
    for pixel in range(720, 723):
        color = pyautogui.pixel(pixel, pixel)[0]
        if color >= 83 and color <= 169:
            pyautogui.press('space')
            pyautogui.sleep(0.1)
            pyautogui.press('down')
            break
