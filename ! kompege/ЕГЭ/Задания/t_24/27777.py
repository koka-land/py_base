#1
from re import finditer
sp = max(len(i.group()) for i in finditer(r'[1-9AB]*', open('files/24_27777.txt').readline()))
print(sp)

#2
from string import *
s = open('files/24_27777.txt').readline()
no_s = ascii_uppercase[2:]
for i in no_s:
    s = s.replace(i, ' ')
while '  ' in s:
    s = s.replace('  ', ' ')
sp = s.split(' ')
ans = 0
for i in sp:
    ans = max(ans, len(i))
print(ans)
