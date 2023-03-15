f = open('files/17_6752.txt', 'r')
count_3 = 0
count = 0
max = (10**10) * -1

sp = [int(i) for i in f]


for i in sp:
    if i % 3 == 0:
        count_3 += 1

for i in range(len(sp) - 2):
    if ((sp[i] < 0) or (sp[i+1] < 0)) and ((sp[i] + sp[i+1]) < count_3):
        count += 1
        if (sp[i] + sp[i+1]) > max:
            max = (sp[i] + sp[i+1])

print(count, max)