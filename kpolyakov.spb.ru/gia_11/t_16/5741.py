'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5741
'''

def f(n):
    if n >= 10000:
        return n
    if (n % 2 == 0) and (n < 10000):
        return f(n+1) + n*n - 3 * (n - 1)
    if (n % 2 == 1) and (n < 10000):
        return f(n + 2) + 4 * n + 1

print(f(9950) - f(9999))