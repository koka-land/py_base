from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Тест 1')
root.geometry('760x540')
root.resizable(0, 0)

def hide_but(widget):
    widget.pack_forget()

def show_but(widget):
    # This will recover the widget from toplevel
    widget.pack()

but = Button(root, text='Построить фигуру', command=lambda: hide_but(but))
but.pack()


root.mainloop()