
import math
import tkinter as tk
from tkinter import Label, Entry, Button

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_square_area(side):
    return side**2

def calculate_parallelogram_area(base, height):
    return base * height

def show_fields_for_shape(shape):
    # Hide all fields
    entry_base.grid_remove()
    entry_height.grid_remove()
    entry_length.grid_remove()
    entry_width.grid_remove()
    entry_radius.grid_remove()
    entry_side.grid_remove()
    entry_base_par.grid_remove()
    entry_height_par.grid_remove()

    # Show fields relevant to the selected shape
    if shape == "Triangle":
        entry_base.grid()
        entry_height.grid()
    elif shape == "Rectangle":
        entry_length.grid()
        entry_width.grid()
    elif shape == "Circle":
        entry_radius.grid()
    elif shape == "Square":
        entry_side.grid()
    elif shape == "Parallelogram":
        entry_base_par.grid()
        entry_height_par.grid()

def calculate_and_display_area():
    shape = selected_shape.get()
    show_fields_for_shape(shape)

    if shape == "Triangle":
        area = calculate_triangle_area(float(entry_base.get()), float(entry_height.get()))
    elif shape == "Rectangle":
        area = calculate_rectangle_area(float(entry_length.get()), float(entry_width.get()))
    elif shape == "Circle":
        area = calculate_circle_area(float(entry_radius.get()))
    elif shape == "Square":
        area = calculate_square_area(float(entry_side.get()))
    elif shape == "Parallelogram":
        area = calculate_parallelogram_area(float(entry_base_par.get()), float(entry_height_par.get()))
    else:
        area = 0

    result_label.config(text=f"The area of the {shape.lower()} is: {area:.2f}")

# Create the main window
window = tk.Tk()
window.title("Area Calculator")

# Create and place Entry widgets for user input
label_shape = Label(window, text="Select Shape:")
label_shape.grid(row=0, column=0, padx=10, pady=10)

shapes = ["Triangle", "Rectangle", "Circle", "Square", "Parallelogram"]
selected_shape = tk.StringVar()
shape_menu = tk.OptionMenu(window, selected_shape, *shapes, command=lambda x: show_fields_for_shape(x))
shape_menu.grid(row=0, column=1, padx=10, pady=10)

label_base = Label(window, text="Base:")
label_base.grid(row=1, column=0, padx=10, pady=10)
entry_base = Entry(window)
entry_base.grid(row=1, column=1, padx=10, pady=10)

label_height = Label(window, text="Height:")
label_height.grid(row=2, column=0, padx=10, pady=10)
entry_height = Entry(window)
entry_height.grid(row=2, column=1, padx=10, pady=10)

label_length = Label(window, text="Length:")
label_length.grid(row=3, column=0, padx=10, pady=10)
entry_length = Entry(window)
entry_length.grid(row=3, column=1, padx=10, pady=10)

label_width = Label(window, text="Width:")
label_width.grid(row=4, column=0, padx=10, pady=10)
entry_width = Entry(window)
entry_width.grid(row=4, column=1, padx=10, pady=10)

label_radius = Label(window, text="Radius:")
label_radius.grid(row=5, column=0, padx=10, pady=10)
entry_radius = Entry(window)
entry_radius.grid(row=5, column=1, padx=10, pady=10)

label_side = Label(window, text="Side:")
label_side.grid(row=6, column=0, padx=10, pady=10)
entry_side = Entry(window)
entry_side.grid(row=6, column=1, padx=10, pady=10)

label_base_par = Label(window, text="Base:")
label_base_par.grid(row=7, column=0, padx=10, pady=10)
entry_base_par = Entry(window)
entry_base_par.grid(row=7, column=1, padx=10, pady=10)

label_height_par = Label(window, text="Height:")
label_height_par.grid(row=8, column=0, padx=10, pady=10)
entry_height_par = Entry(window)
entry_height_par.grid(row=8, column=1, padx=10, pady=10)

# Create a Button widget to trigger the calculation
calculate_button = Button(window, text="Calculate Area", command=calculate_and_display_area)
calculate_button.grid(row=9, column=0, columnspan=2, pady=10)

# Create a Label widget to display the result
result_label = Label(window, text="")
result_label.grid(row=10, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
