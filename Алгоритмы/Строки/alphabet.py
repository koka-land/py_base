#Способ 1

s = ''

for i in range(ord('A'), ord('Z') + 1):
    s = s + chr(i)

print(s)

#Способ 2

import string

s = string.ascii_uppercase

print(s)


