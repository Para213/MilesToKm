from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=150, height=150)
window.eval('tk::PlaceWindow . center')
window.config(padx=50, pady=50)

#mile label

mile_label = Label(text="Miles", font=("Arial", 16))
mile_label.grid(row=0, column=2)

#km label

km_label = Label(text="Km", font=("Arial", 16))
km_label.grid(row=1, column=2)

#km label

rez_label = Label(text="0", font=("Arial", 16, "bold"))
rez_label.grid(row=1, column=1)

#km label

eq_label = Label(text="is equal to", font=("Arial", 16))
eq_label.grid(row=1, column=0)
#Button

def button_clicked():
    mile = float(input.get())
    rez_label.config(text=round(1.609344 * mile, 2))

button = Button(text="Click Me", command=button_clicked)
button.grid(row=2, column=1)

#Input

input = Entry(width=10)
input.grid(row=0, column=1)

window.mainloop()
