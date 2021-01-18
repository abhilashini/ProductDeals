from tkinter import *


def miles_to_km():
	miles = float(miles_entry.get())
	km = round(miles*1.609, 3)
	calc_km_lbl.config(text=f"{km}")

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=150, height=100)
window.config(padx=20, pady=20)

lbl = Label(text="is equal to")
lbl.grid(column=0, row=1)
lbl.config(padx=10, pady=10)

miles_entry = Entry(text=0, width=8)
miles_entry.grid(column=1, row=0)

calc_km_lbl = Label(text=0)
calc_km_lbl.grid(column=1, row=1)

calc_btn = Button(text="Convert", command=miles_to_km)
calc_btn.grid(column=1, row=2)

miles_lbl = Label(text="Miles")
miles_lbl.grid(column=2, row=0)
miles_lbl.config(padx=10, pady=10)

km_lbl = Label(text="KM")
km_lbl.grid(column=2, row=1)
km_lbl.config(padx=10, pady=10)

window.mainloop()