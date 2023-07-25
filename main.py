from tkinter import *

# Create window
window = Tk()
window.title("Miles to KM")

window.minsize(width=200, height=100)

# Adding text
text_one = Label(text="is equal to")
text_one.grid(column=0, row=1)
text_one.config(padx=20)

# Input box
box_one = Entry(width=10)
box_one.grid(column=1, row=0)

# Function that does the conversion from miles to kilometres
def button_calculation():
    miles_to_km = float(box_one.get()) * 1.609
    text_three.config(text=miles_to_km)

# Adding more text
text_two = Label(text="miles")
text_two.grid(column=2, row=0)

text_three = Label(text="0")
text_three.grid(column=1, row=1)

text_four = Label(text="kilometers")
text_four.grid(column=2, row=1)

# Button that will do the calculation when clicked
button = Button(text="Calculate", command=button_calculation)
button.grid(column=1, row=2)

window.mainloop()
