import string
alph = string.digits + string.ascii_uppercase

a = int(input())
ss = int(input())
answer = ''

while a > 0:
    answer = alph[a % ss] + answer
    a = a // ss

print(answer)

