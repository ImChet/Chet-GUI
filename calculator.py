import sys
import math
import tkinter as tk
from tkinter import messagebox


# Sets up the calculator GUI
def calculatorGUI():
    # Spawns a new window
    main_frame = tk.Toplevel()
    # Pulls the window to the front
    main_frame.lift()
    main_frame.attributes('-topmost', True)
    main_frame.after_idle(main_frame.attributes, '-topmost', False)
    # Sets the Chet logo
    main_frame.iconbitmap("chet-logo.ico")
    # Sets the title of the window
    # main_frame.title("Chet\'s Calculator")
    main_frame.title("")
    # Sets up the size of the window  (width, height)
    main_frame.minsize(250, 400)
    main_frame.maxsize(250, 400)
    main_frame.geometry('250x400')

    # Buttons
    frame_A = tk.Frame(main_frame)
    frame_A.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    # Grid configurations
    frame_A.grid_rowconfigure(0, weight=0)
    frame_A.grid_rowconfigure(1, weight=1)
    frame_A.grid_rowconfigure(2, weight=1)
    frame_A.grid_rowconfigure(3, weight=1)
    frame_A.grid_rowconfigure(4, weight=1)
    frame_A.grid_rowconfigure(5, weight=1)
    frame_A.grid_rowconfigure(6, weight=1)
    frame_A.grid_rowconfigure(7, weight=1)

    frame_A.grid_columnconfigure(0, weight=1)
    frame_A.grid_columnconfigure(1, weight=1)
    frame_A.grid_columnconfigure(2, weight=1)
    frame_A.grid_columnconfigure(3, weight=1)

    # Variables
    main_calculation_var = tk.StringVar(value='')
    running_calculation = []

    # Title of window
    # Row 0
    main_title = tk.Label(frame_A, text='Chet\'s Calculator', font=("Arial", 15, "bold"), relief="flat")
    main_title.grid(row=0, column=0, columnspan=4, sticky=tk.EW)

    # Row 1
    calculations_label = tk.Label(frame_A, textvariable=main_calculation_var, font=("Arial", 10, "bold"), borderwidth=5, relief="groove", border=1)
    calculations_label.grid(row=1, column=0, columnspan=4, sticky=tk.EW)

    # Row 2

    def sqrtCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation:
            if current_calculation[-1] not in ['+', '-', '/', '*']:
                sqrt_of = (math.sqrt(eval(current_calculation)))
                main_calculation_var.set(value=f'{str(sqrt_of)}')

    sqrt_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="√",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=sqrtCommand, font=("Arial", 10, "bold"))
    sqrt_button.grid(row=2, column=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def squaredCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation:
            if current_calculation[-1] not in ['+', '-', '/', '*']:
                main_calculation_var.set(value=f'{str(eval(current_calculation)**2)}')

    squared_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="x^2",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=squaredCommand, font=("Arial", 10, "bold"))
    squared_button.grid(row=2, column=1, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def clearCommand():
        main_calculation_var.set(value='')

    clear_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="Clear",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=clearCommand, font=("Arial", 10, "bold"))
    clear_button.grid(row=2, column=2, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def backspaceCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=current_calculation[:-1])

    backspace_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="←",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=backspaceCommand, font=("Arial", 10, "bold"))
    backspace_button.grid(row=2, column=3, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # Row 3

    def sevenCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}{7}')

    seven_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="7",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=sevenCommand, font=("Arial", 10, "bold"))
    seven_button.grid(row=3, column=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def eightCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}{8}')

    eight_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="8",
                               background="#DCDCDC",
                               activebackground="#CACACA", command=eightCommand, font=("Arial", 10, "bold"))
    eight_button.grid(row=3, column=1, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def nineCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}{9}')

    nine_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="9",
                             background="#DCDCDC",
                             activebackground="#CACACA", command=nineCommand, font=("Arial", 10, "bold"))
    nine_button.grid(row=3, column=2, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def divideCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}/')

    divide_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="/",
                                 background="#DCDCDC",
                                 activebackground="#CACACA", command=divideCommand, font=("Arial", 10, "bold"))
    divide_button.grid(row=3, column=3, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # Row 4

    def fourCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}{4}')

    four_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="4",
                             background="#DCDCDC",
                             activebackground="#CACACA", command=fourCommand, font=("Arial", 10, "bold"))
    four_button.grid(row=4, column=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def fiveCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}{5}')

    five_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="5",
                             background="#DCDCDC",
                             activebackground="#CACACA", command=fiveCommand, font=("Arial", 10, "bold"))
    five_button.grid(row=4, column=1, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def sixCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}{6}')

    six_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="6",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=sixCommand, font=("Arial", 10, "bold"))
    six_button.grid(row=4, column=2, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def multiplyCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}*')

    multiply_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="x",
                              background="#DCDCDC",
                              activebackground="#CACACA", command=multiplyCommand, font=("Arial", 10, "bold"))
    multiply_button.grid(row=4, column=3, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # Row 5

    def oneCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}{1}')

    one_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="1",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=oneCommand, font=("Arial", 10, "bold"))
    one_button.grid(row=5, column=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def twoCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}{2}')

    two_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="2",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=twoCommand, font=("Arial", 10, "bold"))
    two_button.grid(row=5, column=1, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def threeCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}{3}')

    three_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="3",
                           background="#DCDCDC",
                           activebackground="#CACACA", command=threeCommand, font=("Arial", 10, "bold"))
    three_button.grid(row=5, column=2, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def subtractionCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}-')

    subtraction_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="-",
                                background="#DCDCDC",
                                activebackground="#CACACA", command=subtractionCommand, font=("Arial", 10, "bold"))
    subtraction_button.grid(row=5, column=3, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # Row 6

    blank_button = tk.Button(frame_A, borderwidth=3, relief="flat", border=0)
    blank_button.grid(row=6, column=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def zeroCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}{0}')

    zero_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="0",
                           background="#DCDCDC",
                           activebackground="#CACACA", command=zeroCommand, font=("Arial", 10, "bold"))
    zero_button.grid(row=6, column=1, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def decimalCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}.')

    decimal_button = tk.Button(frame_A, borderwidth=3, relief="raised", text=".",
                             background="#DCDCDC",
                             activebackground="#CACACA", command=decimalCommand, font=("Arial", 10, "bold"))
    decimal_button.grid(row=6, column=2, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    def additionCommand():
        current_calculation = main_calculation_var.get()
        main_calculation_var.set(value=f'{current_calculation}+')

    addition_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="+",
                                background="#DCDCDC",
                                activebackground="#CACACA", command=additionCommand, font=("Arial", 10, "bold"))
    addition_button.grid(row=6, column=3, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # Row 7

    def equalsCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation:
            if current_calculation[-1] not in ['+', '-', '/', '*']:
                main_calculation_var.set(value=f'{eval(current_calculation)}')

    equals_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="=",
                                background="#DCDCDC",
                                activebackground="#CACACA", command=equalsCommand, font=("Arial", 10, "bold"))
    equals_button.grid(row=7, column=0, columnspan=4, sticky=tk.NSEW, padx=2, pady=2)

    # Called when the window is closed
    def onWindowClose():
        if messagebox.askyesno("Chet\'s Calculator", "Are you sure that you want to quit?"):
            # Kills the window
            main_frame.destroy()
            # Closes the program entirely
            sys.exit()

    # Sets up a binding for when window is closed to call onWindowClose function
    main_frame.protocol("WM_DELETE_WINDOW", onWindowClose)

