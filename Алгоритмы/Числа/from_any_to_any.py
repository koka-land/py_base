import string

def perevod(x, ss):
    alph = string.digits + string.ascii_uppercase
    res = ''
    while x > 0:
        res = alph[x % ss] + res
        x //= ss
    return(res)

a = input('Введите число для перевода: ')
ss1 = int(input('Введите систему счисления числа: '))
ss2 = int(input('Введите систему счисления для перевода: '))

a = int(a, ss1)
a = perevod(a, ss2)
print(a)
