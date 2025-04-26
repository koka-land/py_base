from tkinter import *
from tkinter import ttk

root = Tk()

def key_handler(event):
    print(event.char, event.keysym, event.keycode)
    label.config(text=event.char.format(Text))

label = Label(text="Position 1 ", bg="yellow", fg="red", width=10, height=5)

label.grid(row=1, column=1)
root.bind("<Key>", key_handler)

root.mainloop()