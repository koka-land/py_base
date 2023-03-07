#1 способ

s = ''

for i in range(ord('A'), ord('Z') + 1):
    s = s + chr(i)

print(s)

#2 способ

import string

s = string.ascii_uppercase

print(s)

