#Способ 1

import string

f = open('../files/24.txt', 'r')
sp = []
alph = string.ascii_uppercase

for i in f:
    s_a = []
    vs = []
    max_s = 0
    for j in range(len(i) - 1):
        if i[j] == 'T':
            s_a.append(i[j] + i[j + 1])
    for j in alph:
        s = 'T' + j
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

#Способ 2
#by Pavel Kudinov

f = open('../files/24.txt', 'r')
t = ''

for s in f:
    a = [s[i + 1] for i in range(len(s) - 1) if s[i] == 'T']
    c = [a.count(i) for i in a]
    t += ''.join(set(a[i] for i in range(len(c)) if c[i] == max(c)))

print(max(t.count(i) for i in t))
