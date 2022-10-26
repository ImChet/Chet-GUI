# Imports
import tkinter as tk
from tkinter import messagebox

import pdf_combiner
import password_generator

# Main GUI Window
main_GUI = tk.Tk()
main_GUI.withdraw()
main_GUI.title("Chet\'s GUI Tools")
main_GUI.minsize(350, 300)
main_GUI.maxsize(350, 300)
main_GUI.geometry('350x300')

frame_A = tk.Frame(main_GUI)
frame_A.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

main_title = tk.Label(frame_A, text='Chet\'s GUI Tools', font=("Arial", 15, "bold"), relief="flat")
main_title.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

main_information = tk.Label(frame_A, text='Choose which tool you would like to use:', font=("Arial", 10, "italic"), relief="flat")
main_information.pack(side=tk.TOP, expand=True)

password_generator_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="Password Generator",
                                      command=lambda: password_generator.passwordGeneratorGUI() & main_GUI.withdraw(), background="#DCDCDC",
                                      activebackground="#CACACA")
password_generator_button.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

pdf_combiner_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="PDF Combiner",
                                      command=lambda: pdf_combiner.fileOperationsGUI() & main_GUI.withdraw(), background="#DCDCDC",
                                      activebackground="#CACACA")
pdf_combiner_button.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


def onWindowClose():
    if messagebox.askyesno("Chet\'s GUI Tools", "Are you sure that you want to quit?"):
        main_GUI.destroy()


main_GUI.protocol("WM_DELETE_WINDOW", onWindowClose)


if __name__ == '__main__':
    main_GUI.deiconify()
    main_GUI.mainloop()
