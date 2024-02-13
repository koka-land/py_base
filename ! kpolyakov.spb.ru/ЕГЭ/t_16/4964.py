'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4964
'''

sp = []

for n in range(500000000):
    if n == 0:
        sp.append(1)
    if (n > 0) and (n % 2 != 0):
        sp.append(1 + sp[n - 1])
    if (n > 0) and (n % 2 == 0):
        sp.append(sp[n // 2])

print(sp.count(3))
