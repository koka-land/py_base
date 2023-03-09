from tkinter import *
from tkinter import ttk

def result():
    for x in range(2):
        for y in range(2):
            a = equation_input.cget("text")
            exec("a = " + str(a) + "\nprint(a)")
def input_var(e):
    x = str(e.widget)[2::]
    res = equation_input.cget("text")
    if x == 'button':
        equation_input.configure(text=res + 'w')
    if x == 'button2':
        equation_input.configure(text=res + 'x')
    if x == 'button3':
        equation_input.configure(text=res + 'y')
    if x == 'button4':
        equation_input.configure(text=res + 'z')
    if x == 'button5':
        equation_input.configure(text=res + '(')
    if x == 'button6':
        equation_input.configure(text=res + ')')
    if x == 'button7':
        equation_input.configure(text=res + ' or ')
    if x == 'button8':
        equation_input.configure(text=res + ' and ')
    if x == 'button9':
        equation_input.configure(text=res + ' \u2192 ')
    if x == 'button10':
        equation_input.configure(text=res + ' \u2261 ')
    if x == 'button11':
        equation_input.configure(text=res + chr(172))


def input_clear():
    res = ''
    equation_input.configure(text=res)

w_booly = Tk()

width = 700
height = 500
screen_width = w_booly.winfo_screenwidth()
screen_height = w_booly.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

w_booly.resizable(False, False)
w_booly.configure(bg='#ECD5BB')

w_booly.title("Booly - Решение логических уравнений")
w_booly.geometry('%dx%d+%d+%d' % (width, height, x, y))

header = Label(text="Booly", fg="#2D1016", bg='#ECD5BB', font=("Tahoma", 50))
header.place(x=30, y=15)
subheader_line1 = Label(text="Решение логических", fg="#2D1016", bg='#ECD5BB', font=("Tahoma", 12))
subheader_line1.place(x=210, y=40)
subheader_line2 = Label(text="уравнений. v.01.01", fg="#2D1016", bg='#ECD5BB', font=("Tahoma", 12))
subheader_line2.place(x=210, y=63)

equation_intro = Label(w_booly, text="Автоматическое решение логических уравнений (задание 2 из ЕГЭ)", fg="#11112C", bg='#ECD5BB', font=("Tahoma", 12))
equation_intro.place(x=30, y=130)

equation_input = Label(w_booly, fg="#11112C", bg='#E9F1F7', font=("Tahoma", 16), width="47")
equation_input.place(x=30, y=170)

btn_w = Button(w_booly, text="w", width=3, fg="#11112C", font=("Tahoma", 16))
btn_w.bind('<Button-1>', input_var)
btn_w.pack()
btn_w.place(x=30, y=210)

btn_x = Button(w_booly, text="x", width=3, fg="#11112C", font=("Tahoma", 16))
btn_x.bind('<Button-1>', input_var)
btn_x.pack()
btn_x.place(x=80, y=210)

btn_y = Button(w_booly, text="y", width=3, fg="#11112C", font=("Tahoma", 16))
btn_y.bind('<Button-1>', input_var)
btn_y.pack()
btn_y.place(x=130, y=210)

btn_z = Button(w_booly, text="z", width=3, fg="#11112C", font=("Tahoma", 16))
btn_z.bind('<Button-1>', input_var)
btn_z.pack()
btn_z.place(x=180, y=210)

btn_o = Button(w_booly, text="(", width=3, fg="#11112C", font=("Tahoma", 16))
btn_o.bind('<Button-1>', input_var)
btn_o.pack()
btn_o.place(x=30, y=260)

btn_c = Button(w_booly, text=")", width=3, fg="#11112C", font=("Tahoma", 16))
btn_c.bind('<Button-1>', input_var)
btn_c.pack()
btn_c.place(x=80, y=260)

btn_or = Button(w_booly, text="or", width=3, fg="#11112C", font=("Tahoma", 16))
btn_or.bind('<Button-1>', input_var)
btn_or.pack()
btn_or.place(x=30, y=310)

btn_and = Button(w_booly, text="and", width=3, fg="#11112C", font=("Tahoma", 16))
btn_and.bind('<Button-1>', input_var)
btn_and.pack()
btn_and.place(x=80, y=310)

btn_imp = Button(w_booly, text="\u2192", width=3, fg="#11112C", font=("Tahoma", 16))
btn_imp.bind('<Button-1>', input_var)
btn_imp.pack()
btn_imp.place(x=130, y=310)

btn_eq = Button(w_booly, text="\u2261", width=3, fg="#11112C", font=("Tahoma", 16))
btn_eq.bind('<Button-1>', input_var)
btn_eq.pack()
btn_eq.place(x=180, y=310)

btn_not = Button(w_booly, text=chr(172), width=3, fg="#11112C", font=("Tahoma", 16))
btn_not.bind('<Button-1>', input_var)
btn_not.pack()
btn_not.place(x=230, y=310)

btn_result = Button(w_booly, text="Составить таблицу", width=20, fg="#11112C", font=("Tahoma", 16), command=result)
btn_result.place(x=30, y=360)

btn_clear = Button(w_booly, text="C", command=input_clear, width=3, fg="#11112C", font=("Tahoma", 16))
btn_clear.place(x=620, y=165)

w_booly.mainloop()

'''

'''