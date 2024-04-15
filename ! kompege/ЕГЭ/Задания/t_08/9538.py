from itertools import product
num = '0123456789ABCDE'
cr2 = '02468ACE'
cr3 = '0369C'

count = 0

for a1, a2, a3, a4, a5 in product(num, repeat=5):
    if a1 != '0':
        if a1 in cr2 and a3 in cr2 and a5 in cr2 and \
           a2 in cr3 and a4 in cr3 or \
           a1 in cr3 and a3 in cr3 and a5 in cr3 and \
           a2 in cr2 and a4 in cr2:
            count += 1

print(count)