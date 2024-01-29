from tkinter import *
from math import sqrt

# Creating the main window
main = Tk()
main.title("CALCULATOR")

# Entry widget for displaying the input and output
SCREEN = Entry(main, font=("arial", 20, "bold"), width=18, justify="right", background="black", foreground="white")
SCREEN.pack(padx=10, pady=(10,0), ipady=10, fill=BOTH)
SCREEN.insert(0, "0")

# Frame for buttons
KEYBOARD = Frame(main)
KEYBOARD.pack(pady=10, padx=10)

# Values of the buttons
BTN = [["C", "x²", "%", "√"],
       ["7", "8", "9", "/"],
       ["4", "5", "6", "x"],
       ["1", "2", "3", "+"],
       [".", "0", "=", "-"]]

# Function to handle button press
def press_btn(text):
    if text == "=":
        result= eval(SCREEN.get().replace("²","**2"))
        SCREEN.delete(0, "end")
        SCREEN.insert(0, result)  
    elif text == "C":
        SCREEN.delete(0, END)  # Clear the entry screen
    elif text == "√":
        result = sqrt(float(SCREEN.get()))
        SCREEN.delete(0, END)
        SCREEN.insert(0, result)
    else:
        if SCREEN.get() == "0":
            SCREEN.delete(0, END)
        SCREEN.insert(END, text.replace("x²", "²").replace("x", "*"))

# Function to create button commands
def create_button(text):
    return lambda: press_btn(text)

# Creating the buttons
for i in range(5):
    for j in range(4):
        text = BTN[i][j]
        command = create_button(text)
        # Creating the button with respective properties
        btn = Button(KEYBOARD, text=text, width=6, height=3, background="#33C1FF", foreground="black", font=("arial", 12, "bold"), command=command)
        btn.grid(row=i, column=j, padx=5, pady=5)

main.mainloop()
