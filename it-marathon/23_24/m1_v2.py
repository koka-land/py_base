from tkinter import *

coords = [[0, 0], [10, 0], [10, 10], [20, 10], [20, 0], [30, 0], [30, 20], [0, 20]]
nc = [0, 0]
root = Tk()
root.title('ИТ марафон')
root.geometry('500x500')

canvas = Canvas(bg='#DFA4E9', width=500, height=500)
canvas.pack(anchor=CENTER, expand=1)

nc[0] = int(input())
nc[1] = int(input())
m = int(input())

max_c = 0

for c in coords:
    for i in range(2):
        c[i] = c[i] * m + nc[i]

max_c = max(c)

if max_c <= 500:
    canvas.create_polygon(coords, fill='#BC38D3', outline='#5D016D', width=2)
else:
    print('Размер фигуры превышает размер поля')

root.mainloop()
