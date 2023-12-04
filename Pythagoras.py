import math
import tkinter as tk
from tkinter import Label, Entry, Button

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def calculate_and_display_hypotenuse():
    # Get the lengths of the legs from the Entry widgets
    a = float(entry_a.get())
    b = float(entry_b.get())

    # Calculate the hypotenuse
    hypotenuse = calculate_hypotenuse(a, b)

    # Display the result in the Label widget
    result_label.config(text=f"The length of the hypotenuse is: {hypotenuse:.2f}")

# Create the main window
window = tk.Tk()
window.title("Pythagorean Theorem Calculator")

# Create and place Entry widgets for user input
label_a = Label(window, text="Length of the first leg:")
label_a.grid(row=0, column=0, padx=10, pady=10)
entry_a = Entry(window)
entry_a.grid(row=0, column=1, padx=10, pady=10)

label_b = Label(window, text="Length of the second leg:")
label_b.grid(row=1, column=0, padx=10, pady=10)
entry_b = Entry(window)
entry_b.grid(row=1, column=1, padx=10, pady=10)

# Create a Button widget to trigger the calculation
calculate_button = Button(window, text="Calculate Hypotenuse", command=calculate_and_display_hypotenuse)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create a Label widget to display the result
result_label = Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
