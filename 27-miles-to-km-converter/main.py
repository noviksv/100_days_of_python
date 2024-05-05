# mile to km converter
from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


#Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

#Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


#Labels
miles_label = Label(text="Miles")
km_result_label = Label(text="0")
is_equal_label = Label(text="is equal to")
km_label = Label(text="Km")
miles_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
km_result_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)

#Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
#calls action() when pressed enter
miles_input.bind("<Return>", lambda event: miles_to_km())

window.mainloop()



