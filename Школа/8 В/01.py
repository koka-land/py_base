n = int(input())

o1 = o2 = o3 = o4 = o5 = o6 = 'None'

for i in range(n):
    a = int(input())
    #***********************************
    if abs(a) % 5 == 0:
        if o1 == 'None':
            o1 = a
        else:
            if a > o1:
                o1 = a
    #***********************************
    if abs(a) % 3 == 0:
        if o2 == 'None':
            o2 = a
        else:
            if a < o2:
                o2 = a
    #***********************************
    if abs(a) % 2 == 0:
        if o3 == 'None':
            o3 = a
        else:
            o3 += a
    else:
        if o4 == 'None':
            o4 = a
        else:
            o4 *= a
    # ***********************************
    if abs(a) % 10 == 7:
        if o5 == 'None':
            o5 = 1
        else:
            o5 += 1
    #***********************************
    if 9 < abs(a) < 100:
        if o6 == 'None':
            o6 = [a]
        else:
            o6.append(a)

print(o1)
print(o2)
print(o3)
print(o4)
print(o5)
if o6 == 'None':
    print(o6)
else:
    print(sum(o6) / len(o6))

#Генераторы

nums = [int(input()) for _ in range(int(input()))]
print(max([i for i in nums if i % 5 == 0]) if [i for i in nums if i % 5 == 0] != [] else "None")
print(min([i for i in nums if i % 3 == 0]) if [i for i in nums if i % 3 == 0] != [] else "None")
print(sum([i for i in nums if i % 2 == 0]) if [i for i in nums if i % 2 == 0] != [] else "None")
from math import prod
print(prod([i for i in nums if i % 2 != 0]) if [i for i in nums if i % 2 != 0] != [] else "None")
print(len([i for i in nums if i % 10 == 7]) if [i for i in nums if i % 10 == 7] != [] else "None")
print(sum([i for i in nums if len(str(abs(i))) == 2]) if [i for i in nums if len(str(abs(i))) == 2] != [] else "None")

a = b = []
print(int(i) for i in range(5))