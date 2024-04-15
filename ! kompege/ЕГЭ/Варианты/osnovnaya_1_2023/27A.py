f = open('files/27_A_9755.txt')

sp = []

k = int(f.readline())
n = int(f.readline())
for i in f:
    sp.append(int(i))

min_troyka = max(sp) ** 10

for a1 in range(0, len(sp) - k * 2):
    for a2 in range(a1 + k, len(sp) - k):
        for a3 in range(a2 + k, len(sp)):
            min_troyka = min(min_troyka, sp[a1] + sp[a2] + sp[a3])

print(min_troyka)
