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
for i in sym:
    ans += i * s.count(i)

print('Выберите способ сортировки')
print('  1 - В алфавитном порядке')
print('  2 - В обратном порядке')
v = input('Ваш выбор: ')

if v == '1':
    print(ans)
else:
    print(ans[::-1])