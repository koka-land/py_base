f = open('files/24_2507.txt')
max_p = 0
max_b = 0
str_ = ''
all_str = ''
sym = ''

for i in f:
    all_str += i
    c = 1
    for j in range(len(i) - 1):
        if i[j] == i[j + 1]:
            c += 1
        else:
            if c > max_p:
                max_p = c
                str_ = i
            c = 1

mn_i = list(set(i[:-2]))
mn_i.sort()

for i in mn_i:
    if str_.count(i) > max_b:
        sym = i
        max_b = str_.count(i)

sum_ = 0

print(sym, all_str.count(sym))



