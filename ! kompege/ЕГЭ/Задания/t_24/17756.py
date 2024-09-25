from itertools import product

f = open('files/24_17756.txt').readline()

c = [''.join(x) for x in product('+*', repeat=2)]
for i in c:
    f = f.replace(i, (i[0] + ' ' + i[1]))

res = f.split(' ')

res_max = [len(x) for x in res]
print(max(res_max))
