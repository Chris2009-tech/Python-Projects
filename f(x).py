import tkinter as tk
from tkinter import messagebox

def calculate_average():
    # Retrieve values from entry widgets
    a = int(entry_list[0].get())
    b = int(entry_list[1].get())
    x = (a + b) / 2

    c = int(entry_list[2].get())
    d = int(entry_list[3].get())
    y = (c + d) / 2

    e = int(entry_list[4].get())
    f = int(entry_list[5].get())
    z = (e + f) / 2

    g = int(entry_list[6].get())
    h = int(entry_list[7].get())
    i = int(entry_list[8].get())
    j = int(entry_list[9].get())
    k = int(entry_list[10].get())
    l = int(entry_list[11].get())
    m = int(entry_list[12].get())
    n = int(entry_list[13].get())
    o = int(entry_list[14].get())
    p = int(entry_list[15].get())
    q = int(entry_list[16].get())
    r = int(entry_list[17].get())
    s = int(entry_list[18].get())

    # Calculate overall average
    MO = (x + y + z + g + h + i + j + k + l + m + n + o + p + q + r + s) / 16

    # Display the result in a messagebox
    messagebox.showinfo("Result", f"Your overall average grade is: {MO:.2f}")

def focus_next_entry(event, entry_list):
    current_entry = event.widget
    index = entry_list.index(current_entry)
    next_index = (index + 1) % len(entry_list)
    entry_list[next_index].focus()

# Create the main window
window = tk.Tk()
window.title("Grade Calculator")

# Create input labels and entry widgets for each subject
subject_labels = [
    "N.Glossa", "N.Logotexnia", "Arxaia", "Eleni", "Texnologia", "Pliroforiki",
    "Mousiki", "Kallitexnika", "Mathimatika", "Fysiki", "Xhmia", "Biologia",
    "Istoria", "K.P.A", "Agglika", "Germanika", "Thriskeutika", "Gymnastiki", "Ergastiria"
]

entry_list = []

for i, label_text in enumerate(subject_labels):
    tk.Label(window, text=f"{label_text}:").grid(row=i, column=0)
    entry = tk.Entry(window)
    entry.grid(row=i, column=1, pady=5)
    entry_list.append(entry)
    entry.bind("<Return>", lambda event, entry_list=entry_list: focus_next_entry(event, entry_list))

# Create a button to calculate the average
calculate_button = tk.Button(window, text="Calculate Average", command=calculate_average)
calculate_button.grid(row=len(subject_labels), column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
window.mainloop()
