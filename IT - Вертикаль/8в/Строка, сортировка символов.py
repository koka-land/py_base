import string
cyrillic = ''
ans = ''

s = input()

for i in range(ord('А'), ord('я') + 1):
    cyrillic += chr(i)
    if i == ord('Е') or i == ord('е'):
        if i == ord('Е'):
            cyrillic += 'Ё'
        else:
            cyrillic += 'ё'

sym = string.digits + string.ascii_uppercase + string.ascii_lowercase + cyrillic
print(sym)
for i in sym:
    ans += i * s.count(i)

print(ans)