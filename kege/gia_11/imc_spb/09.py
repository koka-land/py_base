f = open('files/09_6602.csv', 'r')
count = 0

for i in f:
    sp = list(map(int, i.split(';')))

