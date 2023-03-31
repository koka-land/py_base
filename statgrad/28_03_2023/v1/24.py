import string

f = open('../files/24.txt', 'r')
sp = []
alph = string.ascii_uppercase

for i in f:
    s_a = []
    vs = []
    max_s = 0
    for j in range(len(i) - 1):
        if i[j] == 'A':
            s_a.append(i[j] + i[j + 1])
    for j in alph:
        s = 'A' + j
        if s_a.count(s) > max_s:
            max_s = s_a.count(s)
            vs = []
            vs.append(j)
        elif s_a.count(s) == max_s:
            vs.append(j)

    sp += vs

ans = 0

for i in alph:
    if sp.count(i) > ans:
        ans = sp.count(i)

print(ans)
