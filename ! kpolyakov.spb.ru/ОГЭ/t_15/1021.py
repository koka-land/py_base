n = int(input())
neud = 0
f = 'NO'

for i in range(n):
    a = int(input())
    if a < 5:
        neud += 1
    if a == 10:
        f = 'YES'

print(neud)
print(f)
