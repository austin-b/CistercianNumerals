#!/usr/bin/env python3

"""
GUI program to translate numbers from arabic into Cistercian numerals.

https://en.wikipedia.org/wiki/Cistercian_numerals
"""

#######################
# Imports
#######################
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
import sys


#######################
# Functions
#######################


def draw_stem():
    """Draws stem of Cistercian numeral."""
    canvas.create_line(51, 26, 51, 126, width=3)


def draw_ones(num):
    """Draws all numbers in the ones place."""
    if num == 1:
        canvas.create_line(51, 26, 88, 26, width=3)
    elif num == 2:
        canvas.create_line(51, 56, 88, 56, width=3)
    elif num == 3:
        canvas.create_line(51, 26, 88, 56, width=3)
    elif num == 4:
        canvas.create_line(51, 56, 88, 26, width=3)
    elif num == 5:
        canvas.create_line(51, 26, 88, 26, width=3)
        canvas.create_line(51, 56, 88, 26, width=3)
    elif num == 6:
        canvas.create_line(88, 26, 88, 56, width=3)
    elif num == 7:
        canvas.create_line(51, 26, 88, 26, width=3)
        canvas.create_line(88, 26, 88, 56, width=3)
    elif num == 8:
        canvas.create_line(51, 56, 88, 56, width=3)
        canvas.create_line(88, 26, 88, 56, width=3)
    elif num == 9:
        canvas.create_line(51, 26, 88, 26, width=3)
        canvas.create_line(51, 56, 88, 56, width=3)
        canvas.create_line(88, 26, 88, 56, width=3)


def draw_tens(num):
    """Draws all numbers in the tens place."""
    if num == 1:
        canvas.create_line(51, 26, 13, 26, width=3)
    elif num == 2:
        canvas.create_line(51, 56, 13, 56, width=3)
    elif num == 3:
        canvas.create_line(51, 26, 13, 56, width=3)
    elif num == 4:
        canvas.create_line(51, 56, 13, 26, width=3)
    elif num == 5:
        canvas.create_line(51, 26, 13, 26, width=3)
        canvas.create_line(51, 56, 13, 26, width=3)
    elif num == 6:
        canvas.create_line(13, 26, 13, 56, width=3)
    elif num == 7:
        canvas.create_line(51, 26, 13, 26, width=3)
        canvas.create_line(13, 26, 13, 56, width=3)
    elif num == 8:
        canvas.create_line(51, 56, 13, 56, width=3)
        canvas.create_line(13, 26, 13, 56, width=3)
    elif num == 9:
        canvas.create_line(51, 26, 13, 26, width=3)
        canvas.create_line(51, 56, 13, 56, width=3)
        canvas.create_line(13, 26, 13, 56, width=3)


def draw_hundreds(num):
    """Draws all numbers in the hundreds place."""
    if num == 1:
        canvas.create_line(51, 126, 88, 126, width=3)
    elif num == 2:
        canvas.create_line(51, 96, 88, 96, width=3)
    elif num == 3:
        canvas.create_line(51, 126, 88, 96, width=3)
    elif num == 4:
        canvas.create_line(51, 96, 88, 126, width=3)
    elif num == 5:
        canvas.create_line(51, 126, 88, 126, width=3)
        canvas.create_line(51, 96, 88, 126, width=3)
    elif num == 6:
        canvas.create_line(88, 96, 88, 126, width=3)
    elif num == 7:
        canvas.create_line(51, 126, 88, 126, width=3)
        canvas.create_line(88, 96, 88, 126, width=3)
    elif num == 8:
        canvas.create_line(51, 96, 88, 96, width=3)
        canvas.create_line(88, 96, 88, 126, width=3)
    elif num == 9:
        canvas.create_line(51, 126, 88, 126, width=3)
        canvas.create_line(51, 96, 88, 96, width=3)
        canvas.create_line(88, 96, 88, 126, width=3)


def draw_thousands(num):
    """Draws all numbers in the thousands place."""
    if num == 1:
        canvas.create_line(51, 126, 13, 126, width=3)
    elif num == 2:
        canvas.create_line(51, 96, 13, 96, width=3)
    elif num == 3:
        canvas.create_line(51, 126, 13, 96, width=3)
    elif num == 4:
        canvas.create_line(51, 96, 13, 126, width=3)
    elif num == 5:
        canvas.create_line(51, 126, 13, 126, width=3)
        canvas.create_line(51, 96, 13, 126, width=3)
    elif num == 6:
        canvas.create_line(13, 96, 13, 126, width=3)
    elif num == 7:
        canvas.create_line(51, 126, 13, 126, width=3)
        canvas.create_line(13, 96, 13, 126, width=3)
    elif num == 8:
        canvas.create_line(51, 96, 13, 96, width=3)
        canvas.create_line(13, 96, 13, 126, width=3)
    elif num == 9:
        canvas.create_line(51, 126, 13, 126, width=3)
        canvas.create_line(51, 96, 13, 96, width=3)
        canvas.create_line(13, 96, 13, 126, width=3)


def generate_number(event=None):
    """Processes the number and draws it on the canvas."""
    # TODO: try to find a more efficient way to process these numbers
    try:
        canvas.delete("all")    # clear canvas

        num = number.get()

        if len(num) > 4:
            raise ValueError()

        draw_stem()
        draw_ones(int(num[-1]))
        draw_tens(int(num[-2]))
        draw_hundreds(int(num[-3]))
        draw_thousands(int(num[-4]))
    except IndexError:          # catches errors for above if not long enough
        pass
    except ValueError:          # catches errors for incorrect input
        msg.showerror("Error Box", "Only enter numbers 1-9999")


# display a message box
def about():
    """Shows the about info when clicked from the menu."""
    msg.showinfo("About", """
GUI program to translate numbers from arabic into Cistercian numerals.

https://en.wikipedia.org/wiki/Cistercian_numerals

Created by Thomas Bennett.
    """)


# Exit GUI cleanly
def _quit():
    answer = msg.askyesno("Exit Program", "Are you sure you want to exit?")
    if answer:
        win.quit()
        win.destroy()
        sys.exit()


#######################
# GUI Creation
#######################

win = tk.Tk()
win.title("Cistercian Numerals")

######
# Menu Bar
######

# creating a menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# create menu and add menu items
# tearoff=0 removes the dashed line that appears by default; Without disabling
# this default feature, the user can tear off the menu from the main window.
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# add another menu with a Help | About
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

######
# Main GUI
######

input_frame = ttk.Frame(win)
input_frame.grid(column=0, row=0)

a_label = ttk.Label(input_frame, text="Enter a number (1-9999):")
a_label.grid(column=0, row=0, sticky=tk.W, columnspan=2)

number = tk.StringVar()
number_entered = ttk.Entry(input_frame, width=12, textvariable=number)
number_entered.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

action = ttk.Button(input_frame, text="Generate", command=generate_number)
action.grid(column=1, row=1)

canvas = tk.Canvas(win, width=101, height=150, bg="white")
canvas.grid(column=1, row=0, padx=40, pady=40, rowspan=2)

######
# Misc GUI Management
######

# focus on text box
number_entered.focus()

# bind enter key to generate_number
win.bind('<Return>', generate_number)

#######################
# Start GUI
#######################
win.mainloop()