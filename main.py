from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(height=100, width=300)
window.config(padx=100, pady=50)

input = Entry(width=7)
input.grid(row=1, column=1)

label_1 = Label(text="Miles is equal to", font=("Times new Roman", 12))
label_1.config(padx=10, pady=10)
label_1.grid(row=1, column=2)

label_2 = Label(text=0, font=("Times new Roman", 12))
label_2.config(padx=10)
label_2.grid(row=1, column=3)

label_3 = Label(text="KM", font=("Times new Roman", 12))
label_3.config(padx=10)
label_3.grid(row=1, column=4)


def converter():
    miles = float(input.get())
    km = round(miles * 1.609)
    label_2.config(text=f"{km}")


my_button = Button(text="Calculate", command=converter)
my_button.grid(row=2, column=2)

window.mainloop()
