from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

nc = [0, 0]
figures = ["1 фигура", "2 фигура", "3 фигура"]

def click_but():
    all_coords = [[[0, 0], [10, 0], [10, 10], [20, 10], [20, 20], [10, 20], [10, 30], [0, 30]],
                  [[0, 0], [10, 0], [10, 10], [20, 10], [20, 0], [30, 0], [30, 20], [0, 20]],
                  [[0, 0], [10, 0], [10, 10], [20, 10], [20, 30], [10, 30], [10, 20], [0, 20]]]
    if ex.get() == '' or ey.get() == '' or em.get() == '':
        showinfo("Внимание!", "Не все поля заполнены.")
    else:
        coords = all_coords[figures.index(figs.get())]

        canvas.delete("all")
        nc[0] = int(ex.get())
        nc[1] = int(ey.get())
        m = int(em.get())
        ex.delete(0, END)
        ey.delete(0, END)
        em.delete(0, END)
        for c in coords:
            for i in range(2):
                c[i] = c[i] * m + nc[i]

        max_c = max(c)

        if max_c <= 500:
            canvas.create_polygon(coords, fill='#BC38D3', outline='#5D016D', width=2)
        else:
            showinfo("Внимание!", "Размер фигуры превышает размер поля.")


root = Tk()
root.title('ИТ марафон')
root.geometry('760x540')
root.resizable(0, 0)

figures_var = StringVar(value=figures[0])

lx = Label(text='Смещение X')
ly = Label(text='Смещение Y')
lm = Label(text='Множитель')
ex = Entry()
ey = Entry()
em = Entry()
lf = Label(text='Выберите фигуру')
figs = ttk.Combobox(textvariable=figures_var, values=figures, state="readonly")
but = Button(text='Построить фигуру', command=click_but)
message = Label(text='')
canvas = Canvas(bg='#DFA4E9', width=500, height=500)
lx.place(x=20, y=20)
ly.place(x=20, y=50)
lm.place(x=20, y=80)
ex.place(x=100, y=20)
ey.place(x=100, y=50)
em.place(x=100, y=80)
lf.place(x=20, y=110)
figs.place(x=125, y=110, width=100)
but.place(x=20, y=140, width=210)
message.place(x=20, y=140)
canvas.place(x=240, y=20)

root.mainloop()