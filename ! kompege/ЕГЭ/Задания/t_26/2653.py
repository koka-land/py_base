from collections import Counter
import time

start = time.time()
s = open('files/26_2653.txt')
n = int(s.readline())
sp = []

for i in s:
    sp.append(int(i))

all_weight = []

mn = set(sp)
sp.sort()

weight = [sp[0]]

for i in range(1, len(sp)):
    weight.append(sp[i])
    for j in range(len(weight) - 1):
        weight.append(weight[j] + sp[i])
    weight = list(set(weight))

print(weight[-1] - len(weight))
#Долгий перебор - нужно ускорить
'''for i in range(weight[-1], 0, -1):
    if i not in weight:
        print(i)
        break'''

for i in range (min(weight), max(weight) + 1):
    all_weight.append(i)

no_weight = list((Counter(all_weight) - Counter(weight)).elements())

'''print(sp)
print(all_weight)
print(weight)
print(no_weight)'''
print(max(no_weight))
end = time.time()
print(end - start)

