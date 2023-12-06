from tkinter import *
from tkinter import ttk
root = Tk()
s = ttk.Style()
s.configure('Red.TLabelframe.Label', font=('courier', 15, 'bold'))
s.configure('Red.TLabelframe.Label', foreground ='red')
s.configure('Red.TLabelframe.Label', background='blue')
lf = ttk.LabelFrame(root, text = "Test", style = "Red.TLabelframe")

Frame(lf, width=100, height=100, bg='black').pack()
lf.pack( anchor = "w", ipadx = 10, ipady = 5, padx = 10,
                  pady = 0, side = "top")
print(s.lookup('Red.TLabelframe.Label', 'font'))
root.mainloop()