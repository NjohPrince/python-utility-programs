from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

VALUE_OF_A_MILE_IN_KM = 1.60934


def convert_to_km():
    try:
        value_in_miles = float(entry.get())
        value_in_km = value_in_miles * VALUE_OF_A_MILE_IN_KM
        result_label["text"] = value_in_km
    except ValueError:
        result_label["text"] = "Invalid input"


# Entry
entry = Entry(width=10)
entry.grid(row=0, column=1)

# Button
calculate = Button(text="Calculate", width=10, command=convert_to_km)
calculate.grid(row=2, column=1)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)
is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)
result_label = Label(text="0")
result_label.grid(row=1, column=1)
km_label = Label(text="Km")
km_label.grid(row=1, column=2)

window.mainloop()
