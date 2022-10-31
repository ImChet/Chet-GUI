import sys
import tkinter as tk
from tkinter import messagebox

import password_generator
import pdf_combiner
from calculator import calculatorGUI

# Creates the main GUI window
main_GUI = tk.Tk()
# Sets the Chet logo
main_GUI.iconbitmap("chet-logo.ico")
# Sets the title of the window
# main_GUI.title("Chet\'s GUI Tools")
main_GUI.title("")
# Sets up the size of the window
main_GUI.minsize(350, 300)
main_GUI.maxsize(350, 300)
main_GUI.geometry('350x300')

# Grid configurations
main_GUI.grid_rowconfigure(0, weight=1)
main_GUI.grid_columnconfigure(0, weight=1)
main_GUI.grid_rowconfigure(1, weight=1)
# main_GUI.grid_columnconfigure(1, weight=1)
main_GUI.grid_rowconfigure(2, weight=1)
# main_GUI.grid_columnconfigure(2, weight=1)
main_GUI.grid_rowconfigure(3, weight=1)
# main_GUI.grid_columnconfigure(3, weight=1)
main_GUI.grid_rowconfigure(4, weight=1)

# Sets up the title label for the main GUI window
main_title = tk.Label(main_GUI, text='Chet\'s GUI Tools', font=("Arial", 15, "bold"), relief="flat")
main_title.grid(row=0, column=0, sticky=tk.EW)

# Sets up the informational label for the main GUI window
main_information = tk.Label(main_GUI, text='Choose which tool you would like to use:', font=("Arial", 10, "italic"), relief="flat")
main_information.grid(row=1, column=0, sticky=tk.EW)

# Sets up the button that leads to the password generator GUI
password_generator_button = tk.Button(main_GUI, borderwidth=3, relief="raised", text="Password Generator",
                                      command=lambda: exec(f'{password_generator.passwordGeneratorGUI()}\n{main_GUI.withdraw()}'), background="#DCDCDC",
                                      activebackground="#CACACA")
password_generator_button.grid(row=2, column=0, sticky=tk.NSEW, padx=5, pady=3)

# Sets up the button that leads to the PDF combiner GUI
pdf_combiner_button = tk.Button(main_GUI, borderwidth=3, relief="raised", text="PDF Combiner",
                                      command=lambda: exec(f'{pdf_combiner.fileOperationsGUI()}\n{main_GUI.withdraw()}'), background="#DCDCDC",
                                      activebackground="#CACACA")
pdf_combiner_button.grid(row=3, column=0, sticky=tk.NSEW, padx=5, pady=3)

# Sets up the button that leads to the simple calculator GUI
calc_button = tk.Button(main_GUI, borderwidth=3, relief="raised", text="Simple Calculator",
                                      command=lambda: exec(f'{calculatorGUI()}\n{main_GUI.withdraw()}'), background="#DCDCDC",
                                      activebackground="#CACACA")
calc_button.grid(row=4, column=0, sticky=tk.NSEW, padx=5, pady=3)

# Called when the window is closed
def onWindowClose():
    if messagebox.askyesno("Chet\'s GUI Tools", "Are you sure that you want to quit?"):
        # Kills the window
        main_GUI.destroy()
        # Closes the program entirely
        sys.exit()


# Sets up a binding for when window is closed to call onWindowClose function
main_GUI.protocol("WM_DELETE_WINDOW", onWindowClose)

if __name__ == '__main__':
    main_GUI.mainloop()
