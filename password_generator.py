import random
import sys
import time
import tkinter as tk
from tkinter import messagebox

import pyperclip as pc


# Function that creates the randomized password
def passwordGenerator(lowercase_include: bool,
                      uppercase_include: bool,
                      special_include: bool,
                      numbers_include: bool,
                      length: int):

    # Variables
    lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_list = ['!', '@', '#', '$', '%', '&']
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    initial_list = []

    # Options to add to the list for password to be generated off of
    if lowercase_include:
        initial_list = initial_list + lowercase_list
    if uppercase_include:
        initial_list = initial_list + uppercase_list
    if special_include:
        initial_list = initial_list + special_list
    if numbers_include:
        initial_list = initial_list + numbers_list

    # Password Generation
    password = ''.join([str(item) for item in random.choices(initial_list, k=length)])
    return password


# Sets up the password generator GUI
def passwordGeneratorGUI():
    # Spawns a new window
    main_frame = tk.Toplevel()
    # Pulls the window to the front
    main_frame.lift()
    main_frame.attributes('-topmost', True)
    main_frame.after_idle(main_frame.attributes, '-topmost', False)
    # Sets the Chet logo
    main_frame.iconbitmap("chet-logo.ico")
    # Sets the title of the window
    main_frame.title("Chet\'s Password Generator")
    # Sets up the size of the window
    main_frame.minsize(350, 300)
    main_frame.maxsize(350, 300)
    main_frame.geometry('350x300')

    # Sets up the frame for the title of the window
    frame_A = tk.Frame(main_frame)
    frame_A.pack(fill=tk.BOTH, side=tk.TOP, expand=False)
    # Sets up the frame for the user password options
    frame_B = tk.Frame(main_frame)
    frame_B.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    # Sets up the frame for the generate password and copy password filepath buttons
    frame_C = tk.Frame(main_frame)
    frame_C.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

    # Variables/Functions
    lowercase = tk.BooleanVar(value=True)
    uppercase = tk.BooleanVar(value=True)
    special = tk.BooleanVar(value=True)
    numbers = tk.BooleanVar(value=True)
    length_var = tk.IntVar(value=15)  # Default 15
    password_var = tk.StringVar(value='Generate your password...')

    # Functions to get and set user options for password generations
    def setLowercase():
        value = lowercase.get()
        return value

    def setUppercase():
        value = uppercase.get()
        return value

    def setSpecial():
        value = special.get()
        return value

    def setNumber():
        value = numbers.get()
        return value

    # Called when user clicks the generate password button
    def createPassword():
        password = passwordGenerator(setLowercase(), setUppercase(), setSpecial(), setNumber(), length_var.get())
        password_var.set(password)


    # Called when user clicks the copy password button
    def copyToClipboard():
        value = str(password_var.get())
        default_value_check = value == 'Generate your password...'
        if default_value_check is False:
            password_var.set(value='Password Copied...')
            pc.copy(value)

    # Called when the window is closed
    def onWindowClose():
        if messagebox.askyesno("Chet's Password Generator", "Are you sure that you want to quit?"):
            # Kills the window
            main_frame.destroy()
            # Closes the program entirely
            sys.exit()

    # Labels and Buttons // Options (lowercase, uppercase, special, numbers, length)
    password_information = tk.Label(frame_A, text='Chet\'s Password Generator', font=("Arial", 15, "bold"), relief="flat")
    password_information.pack(side=tk.TOP, expand=True)

    options_information = tk.Label(frame_B, text='Select your password complexity:', font=("Arial", 10, "italic"), relief="flat")
    options_information.pack(side=tk.TOP, expand=True)

    length_information = tk.Label(frame_B, text='Desired length:', font=("Arial", 10), relief="flat")
    length_information.pack(side=tk.TOP, expand=True)

    length_spinbox = tk.Spinbox(frame_B, from_=1, to=100, textvariable=length_var, font=("Arial", 10, "italic"), justify="center")
    length_spinbox.pack(side=tk.TOP, expand=True)

    lowercase_checkmark = tk.Checkbutton(frame_B, text='Include Lowercase Characters', variable=lowercase, onvalue=True, offvalue=False, command=setLowercase)
    lowercase_checkmark.pack(side=tk.TOP, expand=True)

    uppercase_checkmark = tk.Checkbutton(frame_B, text='Include Uppercase Characters', variable=uppercase, onvalue=True, offvalue=False, command=setUppercase)
    uppercase_checkmark.pack(side=tk.TOP, expand=True)

    special_checkmark = tk.Checkbutton(frame_B, text='Include Special Characters', variable=special, onvalue=True, offvalue=False, command=setSpecial)
    special_checkmark.pack(side=tk.TOP, expand=True)

    number_checkmark = tk.Checkbutton(frame_B, text='Include Numbers', variable=numbers, onvalue=True, offvalue=False, command=setNumber)
    number_checkmark.pack(side=tk.TOP, expand=True)

    password_actual = tk.Label(frame_B, textvariable=password_var, font=("Arial", 10), borderwidth=5, relief="groove", border=1)
    password_actual.pack(side=tk.TOP, expand=True)

    generate_password_button = tk.Button(frame_C, borderwidth=3, relief="raised", text="Generate Password", command=createPassword, background="#DCDCDC", activebackground="#CACACA")
    generate_password_button.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH)

    copy_password_button = tk.Button(frame_C, borderwidth=3, relief="raised", text='Copy Password', command=copyToClipboard, background="#DCDCDC", activebackground="#CACACA")
    copy_password_button.pack(side=tk.RIGHT, expand=tk.TRUE, fill=tk.BOTH)

    # Sets up a binding for when window is closed to call onWindowClose function
    main_frame.protocol("WM_DELETE_WINDOW", onWindowClose)
    # Keeps the password generator window on top
    main_frame.grab_set()
