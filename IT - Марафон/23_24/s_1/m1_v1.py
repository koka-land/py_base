from tkinter import *

coords = [[0, 0], [10, 0], [10, 10], [20, 10], [20, 20], [10, 20], [10, 30], [0, 30]]

root = Tk()
root.title('ИТ марафон')
root.geometry('500x500')

canvas = Canvas(bg='#DFA4E9', width=500, height=500)
canvas.pack(anchor=CENTER, expand=1)

x = int(input())
y = int(input())
m = int(input())

max_x = 0
max_y = 0

for c in coords:
    c[0] = c[0] * m + x
    max_x = max(c[0], max_x)
    c[1] = c[1] * m + y
    max_y = max(c[1], max_y)

if max_x <= 500 and max_y <= 500:
    canvas.create_polygon(coords, fill='#BC38D3', outline='#5D016D', width=2)
else:
    print('Размер фигуры превышает размер поля')

root.mainloop()
