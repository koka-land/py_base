from tkinter import *

game = Tk()

width, height = 600, 600
screen_width, screen_height = game.winfo_screenwidth(), game.winfo_screenheight()
x, y = (screen_width/2) - (width/2), (screen_height/2) - (height/2)

game.geometry('%dx%d+%d+%d' % (width, height, x, y))
game.title('Угадайка')

label_a = Label(game, text='Label A', bg='yellow', anchor=E)
label_b = Label(game, text='Label A', bg='yellow', anchor=E)
opts = {'padx': 50, 'pady': 20, 'fill': BOTH }
label_a.pack(side=TOP, **opts)
label_b.place(x=140, y=233)

game.mainloop()
