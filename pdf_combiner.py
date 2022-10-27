import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilenames
from PyPDF2 import PdfFileMerger
import pyperclip as pc
import sys


# Sets up the PDF combiner GUI
def fileOperationsGUI():
    # Spawns a new window
    main_frame = tk.Toplevel()
    # Sets the title of the window
    main_frame.title("Chet\'s PDF Combiner")
    # Sets up the size of the window
    main_frame.minsize(700, 300)
    main_frame.maxsize(700, 300)
    main_frame.geometry('700x300')

    # Buttons
    frame_A = tk.Frame(main_frame)
    frame_A.pack(fill=tk.X, side=tk.TOP, expand=True)

    # Desired order of combinations // Packed when files are chosen
    frame_B = tk.Frame(main_frame)

    # Title of window
    main_title = tk.Label(frame_A, text='Chet\'s PDF Combiner', font=("Arial", 15, "bold"),
                                    relief="flat")
    main_title.pack(fill=tk.X, side=tk.TOP, expand=True)

    # Variables
    combined_information_var = tk.StringVar(value='')
    hint_information_var = tk.StringVar(value='Select where you would like your combined PDF file to save...')
    save_dir = ''
    outfile = ''
    userfiles_list_raw = []
    userfiles_list_cleaned = []
    selected_order_list = []
    item_selected_index = 0

    # Information about PDF combiner
    main_information = tk.Label(frame_A, textvariable=hint_information_var, font=("Arial", 10, "italic"),
                                relief="flat")
    main_information.pack(fill=tk.X, side=tk.TOP, expand=True)

    # Gets the desired directory to output the combined file to
    def getSaveDir():
        nonlocal save_dir
        # Prompts the user to select a directory/folder in the file explorer
        save_dir = filedialog.askdirectory()
        # Updates hint
        hint_information_var.set(value='Choose what files to combine...')
        # Shows the choose file button
        file_button.pack(fill=tk.X, side=tk.TOP, expand=True)
        # Delete the select save directory button
        choose_save_dir.destroy()

    # Choose save directory button
    choose_save_dir = tk.Button(frame_A, borderwidth=3, relief="raised", text="Desired Save Directory",
                            command=getSaveDir, background="#DCDCDC",
                            activebackground="#CACACA")
    choose_save_dir.pack(fill=tk.X, side=tk.TOP, expand=True)

    # Shows the current order of chosen files // Shown when files are chosen
    original_order_information = tk.Label(frame_B, text='Current Order:',
                                            font=("Arial", 8, "underline"), relief="flat")
    original_order_information.grid(row=0, column=0, columnspan=1, sticky=tk.NS)

    # Shows the selected order of chosen files // Shown when files are chosen
    reordered_information = tk.Label(frame_B, text='Selected Order:',
                                          font=("Arial", 8, "underline"), relief="flat")
    reordered_information.grid(row=0, column=1, columnspan=1, sticky=tk.NS)

    # Sets up the listboxes for desired ordering of PDF combinations
    frame_B.grid_rowconfigure(0, weight=1)
    frame_B.grid_columnconfigure(0, weight=1)
    frame_B.grid_rowconfigure(1, weight=1)
    frame_B.grid_columnconfigure(1, weight=1)
    listbox1 = tk.Listbox(frame_B)
    listbox2 = tk.Listbox(frame_B)
    listbox1.grid(row=1, column=0, sticky=tk.EW)
    listbox2.grid(row=1, column=1, sticky=tk.EW)

    # Called when an item in the listboxes are clicked on
    def onSelect(event):
        nonlocal item_selected_index
        nonlocal selected_order_list

        w = event.widget
        item_selected = w.curselection()[0]
        # Gets the index of the item selected from the original file order
        item_selected_index = int(item_selected)
        # Inserts the cleaned filename of the selected item in the desired order listbox
        indexed_userfiles_list_raw = userfiles_list_cleaned[item_selected_index]
        listbox2.insert("end", indexed_userfiles_list_raw)
        # Inserts the index of the selected item into a list for future use
        selected_order_list.insert(len(selected_order_list), item_selected_index)
        # Updates Hint
        hint_information_var.set(value='When you have selected the combination order you want, combine your files...')
        # Spawn Combine PDF Button
        combine_button.pack(fill=tk.X, side=tk.TOP, expand=True)

    # Called when choose files button is pressed
    def openFile():
        # Delete the choose files button
        file_button.destroy()
        # Prompts the user to select multiple files in the file explorer
        userfiles = askopenfilenames()

        nonlocal userfiles_list_cleaned
        nonlocal userfiles_list_raw
        nonlocal outfile
        # Sets the outfile with the previously obtained save directory location
        outfile = f'{save_dir}/ChetCombined.pdf'

        # Loops through the chosen files
        for file in userfiles:
            # Inserts the absolute path of each file to list for future use
            userfiles_list_raw.insert(len(userfiles_list_raw), os.path.abspath(file))
            # Inserts the cleaned filename of each file to list for future use
            userfiles_list_cleaned.insert(len(userfiles_list_cleaned), os.path.basename(file)[:-4])

        # Loops from the cleaned filename list
        for item in userfiles_list_cleaned:
            # Inserts each cleaned filename into listbox1
            listbox1.insert("end", item)

        # Updates hint
        hint_information_var.set(value='Click the order in which you want your PDFs to combine...')
        # Builds the new frame that houses the desired ordering of the PDF combiner
        frame_B.pack(fill=tk.X, side=tk.BOTTOM, expand=True)
        # Binds the selection of listbox items to the onSelect function
        listbox1.bind('<<ListboxSelect>>', lambda event: exec(f'{onSelect(event)}'))

    # The setup for the choose files button // Hidden until user selects a save directory
    file_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="Choose Files",
                            command=openFile, background="#DCDCDC",
                            activebackground="#CACACA")

    # Called when combine files button pressed // Shows when <= 1 item is selected in the desired order of combination
    def combineFiles():
        # Checks that the user has selected a save directory
        if save_dir != '':
            # Delete the combine files button
            combine_button.destroy()
            # Forgets/removes the frame housing the desired ordering
            frame_B.pack_forget()
            correct_order_list = []
            # Creates the PDF file merger
            merger = PdfFileMerger()

            # Loops through (len(userfiles_list_raw))x times
            for i in range(len(userfiles_list_raw)):
                # Inserts absolute path name in the selected order given by user
                correct_order_list.insert(len(correct_order_list), userfiles_list_raw[selected_order_list[i]])

            # Loops through and merges each PDF together
            for file in correct_order_list:
                merger.append(file)

            # Writes / Saves the combined PDF to the {outfile} location
            merger.write(outfile)
            # Updates Hint
            hint_information_var.set(value='Files combined and saved.\nCopy the filepath to your new file.')
            # Closes the PDF merger
            merger.close()
            # Shows the copy combined filepath button
            copy_outpath.pack(fill=tk.X, side=tk.BOTTOM, expand=True)

    # Sets up the combined files button
    combine_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="Combine PDFs",
                            command=combineFiles, background="#DCDCDC",
                            activebackground="#CACACA")

    # Called when user clicks the copy combined filepath button
    def copySavePath():
        # Delete the copy combined PDF filepath button
        copy_outpath.destroy()
        # Updates Hint
        hint_information_var.set(value='Filepath copied to your clipboard successfully.\nIf you wish to combine more PDFs, click the \'Refresh PDF Combiner\' button.')
        pc.copy(outfile)
        refresh_button.pack(fill=tk.X, side=tk.BOTTOM, expand=True)

    # Sets up the copy combined filepath button
    copy_outpath = tk.Button(frame_A, borderwidth=3, relief="raised", text="Copy Filepath Of Combined PDF",
                            command=copySavePath, background="#DCDCDC",
                            activebackground="#CACACA")

    def refreshFunction():
        main_frame.destroy()
        fileOperationsGUI()

    # Sets up the refresh button
    refresh_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="Refresh PDF Combiner",
                             command=refreshFunction, background="#DCDCDC",
                             activebackground="#CACACA")

    # Called when the window is closed
    def onWindowClose():
        if messagebox.askyesno("Chet's PDF Combiner", "Are you sure that you want to quit?"):
            # Kills the window
            main_frame.destroy()
            # Closes the program entirely
            sys.exit()

    # Sets up a binding for when window is closed to call onWindowClose function
    main_frame.protocol("WM_DELETE_WINDOW", onWindowClose)
    # Keeps the PDF combiner window on top
    main_frame.grab_set()
