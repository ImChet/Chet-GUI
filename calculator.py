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

    # Frame setup
    frame_A = tk.Frame(main_frame)
    frame_A.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    # Grid weight configurations

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

    # Row 0
    # Title of window
    main_title = tk.Label(frame_A, text='Chet\'s Calculator', font=("Arial", 15, "bold"), relief="flat")
    main_title.grid(row=0, column=0, columnspan=4, sticky=tk.EW)

    # Row 1
    # The main area where the current calculations are displayed
    calculations_label = tk.Label(frame_A, textvariable=main_calculation_var, font=("Arial", 10, "bold"), borderwidth=5, relief="groove", border=1)
    calculations_label.grid(row=1, column=0, columnspan=4, sticky=tk.EW)

    # Row 2
    # The Square Root command that is used by the Square Root button
    def sqrtCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation:
            if current_calculation[-1] not in ['+', '-', '/', '*'] and current_calculation != 'Syntax Error...':
                try:
                    sqrt_of = (math.sqrt(eval(current_calculation)))
                    main_calculation_var.set(value=f'{str(sqrt_of)}')
                except SyntaxError:
                    main_calculation_var.set(value=f'Syntax Error...')

    # Setting up the Square Root button
    sqrt_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="√",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=sqrtCommand, font=("Arial", 10, "bold"))
    sqrt_button.grid(row=2, column=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Squared command that is used by the Squared button
    def squaredCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation:
            if current_calculation[-1] not in ['+', '-', '/', '*'] and current_calculation != 'Syntax Error...':
                try:
                    main_calculation_var.set(value=f'{str(eval(current_calculation)**2)}')
                except SyntaxError:
                    main_calculation_var.set(value=f'Syntax Error...')

    # Setting up the Squared button
    squared_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="x^2",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=squaredCommand, font=("Arial", 10, "bold"))
    squared_button.grid(row=2, column=1, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Clear command that is used by the Clear button
    def clearCommand():
        main_calculation_var.set(value='')

    # Setting up the Clear button
    clear_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="Clear",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=clearCommand, font=("Arial", 10, "bold"))
    clear_button.grid(row=2, column=2, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Backspace command that is used by the Backspace button
    def backspaceCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=current_calculation[:-1])

    # Setting up the Backspace button
    backspace_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="←",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=backspaceCommand, font=("Arial", 10, "bold"))
    backspace_button.grid(row=2, column=3, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # Row 3

    # The Seven command that is used by the Seven button
    def sevenCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}{7}')

    # Setting up the Seven button
    seven_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="7",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=sevenCommand, font=("Arial", 10, "bold"))
    seven_button.grid(row=3, column=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Eight command that is used by the Eight button
    def eightCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}{8}')

    # Setting up the Eight button
    eight_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="8",
                               background="#DCDCDC",
                               activebackground="#CACACA", command=eightCommand, font=("Arial", 10, "bold"))
    eight_button.grid(row=3, column=1, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Nine command that is used by the Nine button
    def nineCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}{9}')

    # Setting up the Nine button
    nine_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="9",
                             background="#DCDCDC",
                             activebackground="#CACACA", command=nineCommand, font=("Arial", 10, "bold"))
    nine_button.grid(row=3, column=2, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Divide command that is used by the Divide button
    def divideCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}/')

    # Setting up the Divide button
    divide_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="/",
                                 background="#DCDCDC",
                                 activebackground="#CACACA", command=divideCommand, font=("Arial", 10, "bold"))
    divide_button.grid(row=3, column=3, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # Row 4

    # The Four command that is used by the Four button# Setting up the Eight button
    def fourCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}{4}')

    # Setting up the Four button
    four_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="4",
                             background="#DCDCDC",
                             activebackground="#CACACA", command=fourCommand, font=("Arial", 10, "bold"))
    four_button.grid(row=4, column=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Five command that is used by the Five button
    def fiveCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}{5}')

    # Setting up the Five button
    five_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="5",
                             background="#DCDCDC",
                             activebackground="#CACACA", command=fiveCommand, font=("Arial", 10, "bold"))
    five_button.grid(row=4, column=1, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Six command that is used by the Six button
    def sixCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}{6}')

    # Setting up the Six button
    six_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="6",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=sixCommand, font=("Arial", 10, "bold"))
    six_button.grid(row=4, column=2, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Multiply command that is used by the Multiply button
    def multiplyCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}*')

    # Setting up the Multiply button
    multiply_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="x",
                              background="#DCDCDC",
                              activebackground="#CACACA", command=multiplyCommand, font=("Arial", 10, "bold"))
    multiply_button.grid(row=4, column=3, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # Row 5

    # The One command that is used by the One button
    def oneCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}{1}')

    # Setting up the One button
    one_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="1",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=oneCommand, font=("Arial", 10, "bold"))
    one_button.grid(row=5, column=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Two command that is used by the Two button
    def twoCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}{2}')

    # Setting up the Two button
    two_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="2",
                            background="#DCDCDC",
                            activebackground="#CACACA", command=twoCommand, font=("Arial", 10, "bold"))
    two_button.grid(row=5, column=1, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Three command that is used by the Three button
    def threeCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}{3}')

    # Setting up the Three button
    three_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="3",
                           background="#DCDCDC",
                           activebackground="#CACACA", command=threeCommand, font=("Arial", 10, "bold"))
    three_button.grid(row=5, column=2, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Subtraction command that is used by the Subtraction button
    def subtractionCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}-')

    # Setting up the Subtraction button
    subtraction_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="-",
                                background="#DCDCDC",
                                activebackground="#CACACA", command=subtractionCommand, font=("Arial", 10, "bold"))
    subtraction_button.grid(row=5, column=3, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # Row 6

    # Setting up a Blank button for aesthetic
    blank_button = tk.Button(frame_A, borderwidth=3, relief="flat", border=0)
    blank_button.grid(row=6, column=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Zero command that is used by the Zero button
    def zeroCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}{0}')

    # Setting up the Zero button
    zero_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="0",
                           background="#DCDCDC",
                           activebackground="#CACACA", command=zeroCommand, font=("Arial", 10, "bold"))
    zero_button.grid(row=6, column=1, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Decimal command that is used by the Decimal button
    def decimalCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}.')

    # Setting up the Decimal button
    decimal_button = tk.Button(frame_A, borderwidth=3, relief="raised", text=".",
                             background="#DCDCDC",
                             activebackground="#CACACA", command=decimalCommand, font=("Arial", 10, "bold"))
    decimal_button.grid(row=6, column=2, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # The Addition command that is used by the Addition button# Setting up the Eight button
    def additionCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation != 'Syntax Error...':
            main_calculation_var.set(value=f'{current_calculation}+')

    # Setting up the Addition button
    addition_button = tk.Button(frame_A, borderwidth=3, relief="raised", text="+",
                                background="#DCDCDC",
                                activebackground="#CACACA", command=additionCommand, font=("Arial", 10, "bold"))
    addition_button.grid(row=6, column=3, columnspan=1, sticky=tk.NSEW, padx=2, pady=2)

    # Row 7

    # The Equals command that is used by the Equals button
    def equalsCommand():
        current_calculation = main_calculation_var.get()
        if current_calculation:
            if current_calculation[-1] not in ['+', '-', '/', '*'] and current_calculation != 'Syntax Error...':
                try:
                    main_calculation_var.set(value=f'{eval(current_calculation)}')
                except SyntaxError:
                    main_calculation_var.set(value=f'Syntax Error...')

    # Setting up the Equals button
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

