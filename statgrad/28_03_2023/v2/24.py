import string

f = open('../files/24.txt', 'r')
sp = []
alph = string.ascii_uppercase

for i in f:
    vs = []
    max_s = 0
    for j in alph:
        s = 'T' + j
        if i.count(s) > max_s:
            vs = []
            max_s = i.count(s)
            vs.append(j)
        elif i.count(s) == max_s:
            vs.append(j)
    sp += vs

ans = 0

for i in alph:
    if sp.count(i) > ans:
        ans = sp.count(i)

print(ans)
