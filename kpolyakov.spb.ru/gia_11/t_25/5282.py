'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5282
'''

def divisors(a):
    sp = []
    for i in range(1, int(a ** (1 / 2)) + 1):
        if a % i == 0:
            if i % 2 != 0:
                sp.append(i)
            if (a // i) % 2 != 0:
                sp.append(a // i)
    return sum(sp)

sp = []

for start in range(1404, 10 ** 10):
    if start % 217 == 0:
        break

for i in range(start, 10 ** 7, 217):
    s = str(i)
    if s[0:2] == '14' and s[3] == '4':
        sp.append(i)

for i in range(len(sp) - 7, len(sp)):
    print(sp[i], divisors(sp[i]))


