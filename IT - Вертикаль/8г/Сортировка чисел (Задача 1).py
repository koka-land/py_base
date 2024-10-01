from random import *

num = []
num_ch = []
num_nech = []

for i in range(15):
    a = randint(1, 1000)
    if a % 2 == 0:
        num_ch.append(a)
    else:
        num_ch.append(a + 1)

for i in range(15):
    a = randint(1, 1000)
    if a % 2 != 0:
        num_nech.append(a)
    else:
        num_nech.append(a + 1)

num_ch.sort()
num_nech.sort(reverse=True)
num = num_ch + num_nech

print(num)