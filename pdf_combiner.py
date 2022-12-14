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
    # Pulls the window to the front
    main_frame.lift()
    main_frame.attributes('-topmost', True)
    main_frame.after_idle(main_frame.attributes, '-topmost', False)
    # Sets the Chet logo
    main_frame.iconbitmap("chet-logo.ico")
    # Sets the title of the window
    # main_frame.title("Chet\'s PDF Combiner")
    main_frame.title("")
    # Sets up the size of the window
    main_frame.minsize(400, 280)
    main_frame.maxsize(400, 280)
    main_frame.geometry('400x280')

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
    hint_information_var = tk.StringVar(value='Select where your file will save...')
    filepath_label_var = tk.StringVar(value='')
    save_dir = ''
    outfile = ''
    userfiles_list_raw = []
    userfiles_list_cleaned = []
    selected_order_list = []
    selected_index = 0
    file_selected_counter = 0
    seen_items = set([])

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
    reordered_information = tk.Label(frame_B, text='Desired Order:',
                                          font=("Arial", 8, "underline"), relief="flat")
    reordered_information.grid(row=0, column=1, columnspan=1, sticky=tk.NS)

    # Sets up the listboxes for desired ordering of PDF combinations
    frame_B.grid_rowconfigure(0, weight=1)
    frame_B.grid_columnconfigure(0, weight=1)
    frame_B.grid_rowconfigure(1, weight=1)
    frame_B.grid_columnconfigure(1, weight=1)
    listbox1 = tk.Listbox(frame_B, selectmode=tk.SINGLE, justify="center")
    listbox2 = tk.Listbox(frame_B, exportselection=False, justify="center")
    listbox1.grid(row=1, column=0, sticky=tk.EW)
    listbox2.grid(row=1, column=1, sticky=tk.EW)

    # Called when an item in the listboxes are clicked on
    def onSelect(event):

        nonlocal selected_index
        nonlocal seen_items
        nonlocal selected_order_list
        nonlocal file_selected_counter

        # Starts the event widget
        w = event.widget
        # Doing a try except to handle possible misclick by user
        try:
            # Gets the index of the user-selected item
            selected_index = w.curselection()[0]
        except IndexError:
            pass

        # Takes cleaned up file name from the previously clicked on item
        user_selected = userfiles_list_cleaned[selected_index]

        # Checks that the item is not a duplicate and that the item is not already assigned the '???' value
        if user_selected not in seen_items and user_selected != '???':
            seen_items.add(user_selected)
            listbox2.insert("end", user_selected)
            file_selected_counter += 1

        # Checks that the item is in listbox2 and that the item is not already assigned the '???' value
        if user_selected in listbox2.get(0, listbox2.size()) and user_selected != '???':
            listbox1.delete(selected_index)
            listbox1.insert(selected_index, '???')

        # Inserts the index of the selected item into a list for future use
        selected_order_list.insert(len(selected_order_list), int(selected_index))

        # Updates Hint
        hint_information_var.set(value=f'Select the order that you want your files to combine.\nFiles selected to combine: {file_selected_counter}/{len(userfiles_list_cleaned)}')

        # This gets triggered when all the files provided by the user have been assigned an order to combine
        if listbox2.size() == len(userfiles_list_cleaned):
            # Spawn Combine PDF Button
            combine_button.pack(fill=tk.X, side=tk.TOP, expand=True)
            # Updates Hint
            hint_information_var.set(value='Click the button to combine your files.')
            # Disable the boxes to prompt the user to click the combine files button
            listbox1.configure(exportselection=False, state=tk.DISABLED)
            listbox2.configure(state=tk.DISABLED)

    # Called when choose files button is pressed
    def openFile():
        # Prompts the user to select multiple files in the file explorer
        userfiles = askopenfilenames()
        # Used for checking each user selected file for .pdf filetype
        pdf_check = True
        # Checks each user selected file for .pdf filetype
        for file in userfiles:
            filetype = os.path.basename(file)[-4:]
            if filetype != '.pdf':
                # If one attachment is not a .pdf, prompt user to reselect files...
                pdf_check = False
        # If not PDF, allow them to retry
        if not pdf_check:
            hint_information_var.set(value=f'One or more file(s) you selected were not a PDF.\nTry again:')
        # If all attachments are a .pdf, proceed
        elif pdf_check:
            # Delete the choose files button
            file_button.destroy()

            nonlocal userfiles_list_cleaned
            nonlocal userfiles_list_raw
            nonlocal outfile
            nonlocal filepath_label_var

            # Sets the outfile with the previously obtained save directory location
            outfile = f'{save_dir}/ChetCombined.pdf'
            filepath_label_var.set(value=outfile)

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
            hint_information_var.set(value=f'Select the order that you want your files to combine.\nFiles selected to combine: {file_selected_counter}/{len(userfiles_list_cleaned)}')
            # Builds the new frame that houses the desired ordering of the PDF combiner
            frame_B.pack(fill=tk.X, side=tk.BOTTOM, expand=True)

            # Binds the selection of listbox items to the onSelect function
            listbox1.bind('<Double-Button-1>', lambda event: exec(f'{onSelect(event)}'))

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
            hint_information_var.set(value='Combined PDF saved successfully.\nCopy the filepath to your new file and/or start over.\n')
            # Closes the PDF merger
            merger.close()
            # Shows the filepath as text
            filepath_label.pack(side=tk.TOP, expand=True)
            # Adds an aesthetic blank spacer
            blank_spacer_label.pack(side=tk.TOP, expand=True)
            # Shows the copy combined filepath button
            copy_outpath.pack(fill=tk.X, side=tk.TOP, expand=True)
            # Shows the window refresh button
            refresh_button.pack(fill=tk.X, side=tk.TOP, expand=True)

    # Sets up the combined files button
    combine_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="Combine PDFs",
                            command=combineFiles, background="#DCDCDC",
                            activebackground="#CACACA")

    # Called when user clicks the copy combined filepath button
    def copySavePath():
        # Delete the copy combined PDF filepath button / filepath text / blank spacer
        copy_outpath.destroy()
        filepath_label.destroy()
        blank_spacer_label.destroy()
        # Updates Hint
        hint_information_var.set(value='Filepath copied to your clipboard successfully.\nTo combine more PDFs, refresh the window.')
        pc.copy(outfile)

    # Sets up the copy combined filepath button
    copy_outpath = tk.Button(frame_A, borderwidth=3, relief="raised", text="Copy Filepath Of Combined PDF",
                            command=copySavePath, background="#DCDCDC",
                            activebackground="#CACACA")

    filepath_label = tk.Label(frame_A, textvariable=filepath_label_var, borderwidth=5, relief="groove", border=1)
    blank_spacer_label = tk.Label(frame_A, relief="flat", border=0)

    # Called when the refresh button is called
    def refreshFunction():
        main_frame.destroy()
        # Recursion if called
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
