def prime(x):
    pr = True
    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            pr = False
            return False
            break
    if pr:
        return x

a = input()
sp = []

for i in a:
    sp.append(int(i))
for i in range(3):
    sp.append(int(a[i] + a[i + 1]))
for i in range(2):
    sp.append(int(a[i] + a[i + 1] + a[i + 2]))
sp.append(int(a))
print(sp)

max_ = 0

for i in sp:
    if prime(i) != False:
        max_ = max(max_, prime(i))

print(max_)
