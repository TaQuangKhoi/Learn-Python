import random
import PySimpleGUI as sg
print("This is Dice Rolling Simulator for You")
print("Your point is", random.randint(1, 6))

import PySimpleGUI as sg

filename = sg.popup_get_file('Enter the file you wish to process')
sg.popup('You entered', filename)