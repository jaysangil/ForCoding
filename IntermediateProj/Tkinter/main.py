from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_label_result.config(text=f"{km}")

window = Tk()
window.title("Miles to Min converter")
window.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_input.grid(row=0, column=2)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

km_label_result = Label(text="0")
km_label_result.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)


window.mainloop()