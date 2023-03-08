from tkinter import *
from tkinter import ttk

def input_x():
    res = 'x'
    equation_input.configure(text=res)

w_booly = Tk()

width = 700
height = 500
screen_width = w_booly.winfo_screenwidth()
screen_height = w_booly.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

w_booly.title("Booly - Решение логических уравнений")
w_booly.geometry('%dx%d+%d+%d' % (width, height, x, y))

header = Label(text="Booly", fg="#2D1016", font=("Tahoma", 50))
header.place(x=30, y=15)
subheader_line1 = Label(text="Решение логических", fg="#2D1016", font=("Tahoma", 12))
subheader_line1.place(x=210, y=40)
subheader_line2 = Label(text="уравнений. v.01.01", fg="#2D1016", font=("Tahoma", 12))
subheader_line2.place(x=210, y=63)

equation_intro = Label(w_booly, text="Автоматическое решение логических уравнений (задание 2 из ЕГЭ)", fg="#11112C", font=("Tahoma", 12))
equation_intro.place(x=30, y=130)

equation_input = Entry(w_booly, fg="#11112C", font=("Tahoma", 16), width="58")
equation_input.place(x=30, y=170)

btn_x = Button(w_booly, text="x", command=input_x, width=3, fg="#11112C", font=("Tahoma", 16))
btn_x.place(x=30, y=210)

w_booly.mainloop()

'''
for x in range(2):
    for y in range(2):
        a = (x or y) and (x or not(y))
        print(x, y)
        exec("a = " + str(a) + "\nprint(a)")
'''