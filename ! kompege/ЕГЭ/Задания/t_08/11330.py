import string

a = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'[::-1]
b = 'ИНФОРМАТИКА'[::-1]
c = string.digits + string.ascii_uppercase
d = 'ИНФОРМАТИКА'

ans = 0
s = 0
for i in b:
    ans += a.index(i) * 33**s
    s += 1

print(ans + 1)

e = ''
for i in d:
    e += c[a.index(i)]
print(int(e, 33) + 1)

