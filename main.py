# Imports
import functions
import tkinter as tk
import pyperclip as pc

# Main Window
main_frame = tk.Tk()
main_frame.title("Chet GUI")
main_frame.minsize(350, 300)
main_frame.maxsize(350, 300)
main_frame.geometry('350x300')

# Variables
lowercase = tk.BooleanVar(value=True)
uppercase = tk.BooleanVar(value=True)
special = tk.BooleanVar(value=True)
numbers = tk.BooleanVar(value=True)
length_var = tk.IntVar(value=15)  # Default 15
password_var = tk.StringVar(value='Generate your password...')

frame_A = tk.Frame(main_frame)
frame_A.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame_B = tk.Frame(main_frame)
frame_B.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame_C = tk.Frame(main_frame)
frame_C.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

password_information = tk.Label(frame_A, text='Chet\'s Password Generator', font=("Arial", 15, "bold"), relief="flat")
password_information.pack(side=tk.TOP, expand=True)

# Options (lowercase, uppercase, special, numbers, length)
options_information = tk.Label(frame_B, text='Select your password complexity:', font=("Arial", 10, "italic"), relief="flat")
options_information.pack(side=tk.TOP, expand=True)

length_information = tk.Label(frame_B, text='Desired length:', font=("Arial", 10), relief="flat")
length_information.pack(side=tk.TOP, expand=True)

length_spinbox = tk.Spinbox(frame_B, from_=1, to=100, textvariable=length_var, font=("Arial", 10, "italic"), justify="center")
length_spinbox.pack(side=tk.TOP, expand=True)


def setLowercase():
    value = lowercase.get()
    return value


lowercase_checkmark = tk.Checkbutton(frame_B, text='Include Lowercase Characters', variable=lowercase, onvalue=True, offvalue=False, command=setLowercase)
lowercase_checkmark.pack(side=tk.TOP, expand=True)


def setUppercase():
    value = uppercase.get()
    return value


uppercase_checkmark = tk.Checkbutton(frame_B, text='Include Uppercase Characters', variable=uppercase, onvalue=True, offvalue=False, command=setUppercase)
uppercase_checkmark.pack(side=tk.TOP, expand=True)


def setSpecial():
    value = special.get()
    return value


special_checkmark = tk.Checkbutton(frame_B, text='Include Special Characters', variable=special, onvalue=True, offvalue=False, command=setSpecial)
special_checkmark.pack(side=tk.TOP, expand=True)


def setNumber():
    value = numbers.get()
    return value


number_checkmark = tk.Checkbutton(frame_B, text='Include Numbers', variable=numbers, onvalue=True, offvalue=False, command=setNumber)
number_checkmark.pack(side=tk.TOP, expand=True)


password_actual = tk.Label(frame_B, textvariable=password_var, font=("Arial", 10), borderwidth=5, relief="groove", border=1)
password_actual.pack(side=tk.TOP, expand=True)


def createPassword():
    password = functions.passwordGenerator(setLowercase(), setUppercase(), setSpecial(), setNumber(), length_var.get())
    password_var.set(password)


# bg="#1F8233" activebackground="#BE1400"
generate_password_button = tk.Button(frame_C, borderwidth=3, relief="raised", text="Generate Password", command=createPassword, background="#DCDCDC", activebackground="#CACACA")
generate_password_button.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH)


def copyToClipboard():
    value = str(password_var.get())
    default_value_check = value == 'Generate your password...'
    if default_value_check is False:
        pc.copy(value)

# bg="#4F67FF" activebackground="#BE1400"
copy_password_button = tk.Button(frame_C, borderwidth=3, relief="raised", text="Copy Password", command=copyToClipboard, background="#DCDCDC", activebackground="#CACACA")
copy_password_button.pack(side=tk.RIGHT, expand=tk.TRUE, fill=tk.BOTH)

main_frame.mainloop()
