##коммент

## pycharm

## плагин

## hello

## world

## connection

##

## modules

import tkinter as tk

import keyboard

def show_hello_world():

    root = tk.Tk()

    label = tk.Label(root, text="Hello, World!")

    label.pack()

    root.mainloop()

keyboard.add_hotkey('ctrl+s+u', show_hello_world)

keyboard.wait('esc')  # Чтобы скрипт продолжал работу до нажатия клавиши 'Esc'