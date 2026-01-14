import string

alph = string.digits + string.ascii_uppercase
answer = ''

a1 = input()
ss1 = int(input())
a2 = input()
ss2 = int(input())
ss3 = int(input())
a1 = int(a1, ss1)
a2 = int(a2, ss2)
a3 = a1 + a2

while a3 > 0:
    answer = alph[a3 % ss3] + answer
    a3 = a3 // ss3

print(answer)


