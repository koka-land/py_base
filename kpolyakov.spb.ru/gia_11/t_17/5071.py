f = open('files/17-292.txt', 'r')
count = 0
min_p = 10**10

#Решение через список
'''
sp = list(map(int, f.readlines()))

for i in range(len(sp)-1):
    if abs((sp[i] % 17 - sp[i+1] % 17)) == ((sp[i] % 4) + (sp[i+1] % 4)):
        count += 1
        if sp[i] + sp[i+1] < min_p:
            min_p = sp[i] + sp[i+1]
'''

#Решение без списка
a = int(f.readline())
b = int(f.readline())

for i in f:
    if abs((a % 17 - b % 17)) == ((a % 4) + (b % 4)):
        print(a, b, abs((a % 17 - b % 17)), (a % 4) + (b % 4))
        count += 1
        if a + b < min_p:
            min_p = a + b
    a = b
    b = i
    if not b:
        break
    else:
        b = int(b)

print(count, min_p)