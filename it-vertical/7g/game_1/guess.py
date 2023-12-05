from tkinter import *

game = Tk()

width = 600
height = 600
screen_width = game.winfo_screenwidth()
screen_height = game.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

game.geometry('%dx%d+%d+%d' % (width, height, x, y))
game.title('Угадайка')

game.mainloop()