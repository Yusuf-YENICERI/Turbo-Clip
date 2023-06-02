

















from pynput import keyboard
import pyperclip
import platform
import time
import os
import functools
from collections import deque

copied_texts = deque(maxlen=4)
key_combinations = [
    {"key": keyboard.Key.ctrl_l, "char": '1'},
    {"key": keyboard.Key.ctrl_l, "char": '2'},
    {"key": keyboard.Key.ctrl_l, "char": '3'},
]
ctrl_pressed = False

def on_activate(i):
    if True:
        if(i > len(copied_texts)):
            return
        pyperclip.copy(copied_texts[-i])

        if platform.system() == "Darwin":  
            controller = keyboard.Controller()
            controller.press(keyboard.Key.cmd_l)
            controller.press('v')
            controller.release('v')
            controller.release(keyboard.Key.cmd_l)
        else: 
            controller = keyboard.Controller()
            controller.press(keyboard.Key.ctrl_l)
            controller.press('v')
            controller.release('v')
            controller.release(keyboard.Key.ctrl_l)

        time.sleep(0.1)


def on_press():
    on_copy()


def on_release(key):
    global ctrl_pressed

    if key == keyboard.Key.esc:
        return False

    if key == keyboard.Key.ctrl_l:
        ctrl_pressed = False


def on_copy():
    copied_text = pyperclip.paste()
    if copied_text:
        copied_texts.append(copied_text)





with keyboard.GlobalHotKeys({
        "<ctrl>+c": functools.partial(on_press),
        "<ctrl>+1": functools.partial(on_activate, 1),
        "<ctrl>+2": functools.partial(on_activate, 2),
        "<ctrl>+3": functools.partial(on_activate, 3),
        "<ctrl>+4": functools.partial(on_activate, 4)
}) as listener:
    listener.join()
    

