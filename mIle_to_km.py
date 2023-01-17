from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

input_space = Entry(width=10)
input_space.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_result = Label(text="0")
label_result.grid(column=1, row=1)

label_km = Label(text="Kilometer")
label_km.grid(column=2, row=1)


def convert():
    mile_input = input_space.get()
    label_result["text"] = round(float(mile_input) * 1.609344)


button = Button(text="Convert", command=convert)
button.grid(column=1, row=2)

window.mainloop()
