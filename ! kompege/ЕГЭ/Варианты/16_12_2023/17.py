f = open('files/17_12249.txt')
sp = []
max_n = 0
max_sum = -10**10
count = 0

for i in f:
    sp.append(int(i))
    if str(sp[-1])[-1] == '3' and \
       len(str(sp[-1])) == 5 and \
       sp[-1] > max_n:
        max_n = sp[-1]

for i in range(0, len(sp) - 2):
    if str(sp[i])[-1] == '3' or \
       str(sp[i + 1])[-1] == '3' or \
       str(sp[i + 2])[-1] == '3':
        if sp[i] + sp[i + 1] + sp[i + 2] <= max_n:
            count += 1
            max_sum = max(max_sum, sp[i] + sp[i + 1] + sp[i + 2])

print(count)
print(max_sum)

