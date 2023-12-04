from tkinter import *

calc = Tk()

width = 300
height = 500

screen_width = calc.winfo_screenwidth()
screen_height = calc.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)


calc.title('Калькулятор')
calc.geometry('%dx%d+%d+%d' % (width, height, x, y))
calc.resizable(0, 0)

def input_var(e):
    x = str(e.widget)[2::]
    if x == 'button':
        screen['text'] = '0'
    if x == 'button2':
        screen['text'] = '1'
    if x == 'button3':
        screen['text'] = '2'
    if x == 'button4':
        screen['text'] = '3'
    if x == 'button5':
        screen['text'] = '4'
    if x == 'button6':
        screen['text'] = '5'
    if x == 'button7':
        screen['text'] = '6'
    if x == 'button8':
        screen['text'] = '7'
    if x == 'button9':
        screen['text'] = '8'
    if x == 'button10':
        screen['text'] = '9'

screen = Label(bg="#AFB0EC",
               width=21,
               height=2,
               text='0',
               anchor="e",
               fg='#080B74',
               font=("PT Sans", 20))

screen.place(x=0, y=0)

btn_0 = Button(calc, text="0", width=5, fg="#080B74", font=("PT Sans", 16))
btn_1 = Button(calc, text="1", width=5, fg="#080B74", font=("PT Sans", 16))
btn_2 = Button(calc, text="2", width=5, fg="#080B74", font=("PT Sans", 16))
btn_3 = Button(calc, text="3", width=5, fg="#080B74", font=("PT Sans", 16))
btn_4 = Button(calc, text="4", width=5, fg="#080B74", font=("PT Sans", 16))
btn_5 = Button(calc, text="5", width=5, fg="#080B74", font=("PT Sans", 16))
btn_6 = Button(calc, text="6", width=5, fg="#080B74", font=("PT Sans", 16))
btn_7 = Button(calc, text="7", width=5, fg="#080B74", font=("PT Sans", 16))
btn_8 = Button(calc, text="8", width=5, fg="#080B74", font=("PT Sans", 16))
btn_9 = Button(calc, text="9", width=5, fg="#080B74", font=("PT Sans", 16))

btn_0.bind('<Button-1>', input_var)
btn_1.bind('<Button-1>', input_var)
btn_2.bind('<Button-1>', input_var)
btn_3.bind('<Button-1>', input_var)
btn_4.bind('<Button-1>', input_var)
btn_5.bind('<Button-1>', input_var)
btn_6.bind('<Button-1>', input_var)
btn_7.bind('<Button-1>', input_var)
btn_8.bind('<Button-1>', input_var)
btn_9.bind('<Button-1>', input_var)

btn_0.place(x=20, y=370)
btn_1.place(x=20, y=310)
btn_2.place(x=90, y=310)
btn_3.place(x=160, y=310)
btn_4.place(x=20, y=250)
btn_5.place(x=90, y=250)
btn_6.place(x=160, y=250)
btn_7.place(x=20, y=190)
btn_8.place(x=90, y=190)
btn_9.place(x=160, y=190)



calc.mainloop()
