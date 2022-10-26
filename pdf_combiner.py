import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilenames
from PyPDF2 import PdfFileMerger


def fileOperationsGUI():
    # Main Window Setup
    main_frame = tk.Toplevel()
    main_frame.title("Chet\'s PDF Combiner")
    main_frame.minsize(350, 300)
    main_frame.maxsize(350, 300)
    main_frame.geometry('350x300')

    frame_A = tk.Frame(main_frame)
    frame_A.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

    main_title = tk.Label(frame_A, text='Chet\'s PDF Combiner', font=("Arial", 15, "bold"),
                                    relief="flat")
    main_title.pack(fill=tk.X, side=tk.TOP, expand=True)

    main_information = tk.Label(frame_A, text='Choose what files to combine:', font=("Arial", 10, "italic"),
                                   relief="flat")
    main_information.pack(fill=tk.X, side=tk.TOP, expand=True)

    # Variables
    combined_information_var = tk.StringVar(value='')

    # Nonlocal Variables
    save_dir = ''
    outfile = ''
    merger = PdfFileMerger()

    def getSaveDir():
        nonlocal save_dir
        save_dir = filedialog.askdirectory()
        print(f'Save dir is: {save_dir}')

    choose_save_dir = tk.Button(frame_A, borderwidth=3, relief="raised", text="Desired Save Directory",
                            command=getSaveDir, background="#DCDCDC",
                            activebackground="#CACACA")
    choose_save_dir.pack(fill=tk.X, side=tk.TOP, expand=True)


    def openFile():
        userfiles = askopenfilenames()
        print(f'Filename(s) raw: {userfiles}')
        print(f'userfiles type: {type(userfiles)}')

        nonlocal merger
        merger = PdfFileMerger()
        for file in userfiles:
            merger.append(file)

        nonlocal outfile
        outfile = f'{save_dir}/ChetCombined.pdf'


    file_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="Open Files",
                            command=openFile, background="#DCDCDC",
                            activebackground="#CACACA")
    file_button.pack(fill=tk.X, side=tk.TOP, expand=True)

    def combineFiles():
        if save_dir != '':
            merger.write(outfile)
            combined_information_var.set(value=f'Files combined and saved...')
            merger.close()

    combine_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="Combine PDFs",
                            command=combineFiles, background="#DCDCDC",
                            activebackground="#CACACA")
    combine_button.pack(fill=tk.X, side=tk.TOP, expand=True)

    combined_information = tk.Label(frame_A, textvariable=combined_information_var, font=("Arial", 10, "italic"), relief="flat")
    combined_information.pack(fill=tk.X, side=tk.TOP, expand=True)

    def onWindowClose():
        if messagebox.askyesno("Chet's PDF Combiner", "Are you sure that you want to quit?"):
            main_frame.destroy()

    main_frame.protocol("WM_DELETE_WINDOW", onWindowClose)
    main_frame.grab_set()

