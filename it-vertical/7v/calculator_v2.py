from tkinter import *
from functools import partial

calc = Tk() #Окно программы

width = 300 #Ширина программы
height = 500 #Выоста программы

screen_width = calc.winfo_screenwidth() #Ширина экрана монитора
screen_height = calc.winfo_screenheight() #Высота экрана монитора

x = (screen_width/2) - (width/2) #Начало окна программы относитель ширины экрана монитора
y = (screen_height/2) - (height/2) #Начало окна программы относительно высота экрана монитора

calc.title('Калькулятор') #Имя окна
calc.geometry('%dx%d+%d+%d' % (width, height, x, y)) #Размещение окна по центру экрана
calc.resizable(0, 0) #Блокировка изменений размера окна

def input_var(e):
    if screen_text['text'] == '0':
        if e != '0':
            screen_text['text'] = e
    else:
        screen_text['text'] = screen_text['text'] + e

screen_frame = Frame(calc,
                     bg="#AFB0EC") #Заливка
screen_text = Label(screen_frame,
                    bg="#AFB0EC", #Заливка
                    text='0', #Текст
                    anchor="e", #Выравнивание по правому краю
                    fg='#080B74', #Цвет текста
                    font=("PT Sans", 20)) #Шрифт и размер
screen_frame.pack(fill=BOTH)
screen_text.pack(fill=BOTH,
                 ipady=40,
                 padx=20)

x = 20 #Начальная координата x для кнопок
y = 430 #Начальная координата y для кнопок

for k in range(10):
    b = Button(calc, text=str(k), width=5, fg="#080B74", font=("PT Sans", 16),
               command=partial(input_var, str(k)))

    if k == 0 or k % 3 == 1:
        x = 20
        y -= 60
    else:
        x += 70

    b.place(x=x, y=y)

calc.mainloop()