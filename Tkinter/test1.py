from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Тест 1')
root.geometry('760x540')
root.resizable(0, 0)

def hide_but(widget):
    widget.place(x=-100, y=-100)

def show_but(widget, a, b):
    # This will recover the widget from toplevel
    widget.place(x=a, y=b)

but = Button(root, text='Построить фигуру', command=lambda: hide_but(but))
but.place(x=20, y=30)
but2 = Button(root, text='Построить фигуру', command=lambda: show_but(but, 20, 30))
but2.place(x=120, y=80)


root.mainloop()