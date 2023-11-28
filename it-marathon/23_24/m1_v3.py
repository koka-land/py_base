from tkinter import *

root = Tk()
root.title('ИТ марафон')
root.geometry('760x540')

lx = Label(text='Смещение X')
ly = Label(text='Смещение Y')
lm = Label(text='Множитель')
ex = Entry()
ey = Entry()
em = Entry()
but = Button(text='Построить фигуру')
canvas = Canvas(bg='#DFA4E9', width=500, height=500)
lx.place(x=20, y=20)
ly.place(x=20, y=50)
lm.place(x=20, y=80)
ex.place(x=100, y=20)
ey.place(x=100, y=50)
em.place(x=100, y=80)
but.place(x=20, y=110, width=210)
canvas.place(x=240, y=20)

root.mainloop()