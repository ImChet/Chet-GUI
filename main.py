import sys
import tkinter as tk
from tkinter import messagebox

import password_generator
import pdf_combiner

# Creates the main GUI window
main_GUI = tk.Tk()
# Hides the main GUI until it is completely setup
main_GUI.withdraw()
# Sets the title of the window
main_GUI.title("Chet\'s GUI Tools")
# Sets up the size of the window
main_GUI.minsize(350, 300)
main_GUI.maxsize(350, 300)
main_GUI.geometry('350x300')

# Creates the frame to work in
frame_A = tk.Frame(main_GUI)
frame_A.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

# Sets up the title label for the main GUI window
main_title = tk.Label(frame_A, text='Chet\'s GUI Tools', font=("Arial", 15, "bold"), relief="flat")
main_title.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# Sets up the informational label for the main GUI window
main_information = tk.Label(frame_A, text='Choose which tool you would like to use:', font=("Arial", 10, "italic"), relief="flat")
main_information.pack(side=tk.TOP, expand=True)

# Sets up the button that leads to the password generator GUI
password_generator_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="Password Generator",
                                      command=lambda: exec(f'{password_generator.passwordGeneratorGUI()}\n{main_GUI.withdraw()}'), background="#DCDCDC",
                                      activebackground="#CACACA")
password_generator_button.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# Sets up the button that leads to the PDF combiner GUI
pdf_combiner_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="PDF Combiner",
                                      command=lambda: exec(f'{pdf_combiner.fileOperationsGUI()}\n{main_GUI.withdraw()}'), background="#DCDCDC",
                                      activebackground="#CACACA")
pdf_combiner_button.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


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
    main_GUI.deiconify()
    main_GUI.mainloop()
