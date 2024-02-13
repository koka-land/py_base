'''
https://kompege.ru/task
'''

count = 0

for i in range(343, 2402):
    s = ''
    while i > 0:
        s = str(i % 7) + s
        i //= 7
    if int(s[-1]) % 2 == 0:
        s = '6' + s
    else:
        s = '5' + s
    if int(s, 7) > 14500:
        count += 1

print(count)
