f = open('files/09_6602.csv', 'r')
count = 0

for i in f:
    sp = sorted(list(map(int, i.split(';'))))
    eq = 0
    num = 0
    sum = 0
    for j in sp:
        sum += j
    for j in range(len(sp) - 2):
        if sp[j] == sp [j+1]:
            eq += 1
            num = sp[j]
    if eq == 1:
        sum -= num * 2
        if (sum // 4) > (num * 2):
        #В задании написано "не меньше", а это значит "больше или равно"
        #При условии (sum // 4) >= (num * 2) находится 65 строк
        #При условии (sum // 4) > (num * 2) находится 64 строки, что соответсвует ответу
            count += 1

print(count)


