'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4884
'''

def prime(n):
    if n == 1:
        return False
    else:
        n = str(n)
        x = 0
        for i in n:
            x = x + int(i)
        f = 0
        for i in range(2, int(x ** (1 / 2)) + 1):
            if x % i == 0:
                f = 1
                break
        if f == 0:
            return True
        else:
            return False

# Решение через рекурсию (долго)

def F(n):
    if n <= 1:
        return 1
    if (n > 1) and (n % 3 == 0):
        return 2 * F(n - 1) + F(n - 2)
    if (n > 1) and (n % 3 != 0):
        return 3 * F(n - 2) + F(n - 1)

for n in range(36):
    if prime(F(n)):
        print(n)

# Решение через список (быстро)

sp = []

for n in range(36):
    if n <= 1:
        sp.append(1)
    if (n > 1) and (n % 3 == 0):
        sp.append(2 * sp[n - 1] + sp[n - 2])
    if (n > 1) and (n % 3 != 0):
        sp.append(3 * sp[n - 2] + sp[n - 1])
    if prime(sp[n]) == True:
        print(n)
