count = 0
str_ = 0
sp_str = []

for i in open('files/9.csv'):
    str_ += 1
    sp = [int(x) for x in i.split(';')]
    a2 = [int(x) for x in sp if sp.count(x) == 2]
    a3 = [int(x) for x in sp if sp.count(x) == 3]
    if len(a2) == 2 and len(a3) == 3 and a3[0] > a2[0]:
        sp_str.append(str_)

print(sp_str[2])