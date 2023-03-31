import string

f = open('../files/24.txt', 'r')
sp = []
alph = string.ascii_uppercase

f = ['ABABACACAAAAAA', 'ACACAAAAAA', 'AAAAAAACACAC']

for i in f:
    print(i)
    vs = []
    max_s = 0
    for j in alph:
        s = 'A' + j
        #print(s, i.count(s))
        if i.count(s) > max_s:
            vs = []
            max_s = i.count(s)
            vs.append(j)
        elif i.count(s) == max_s:
            vs.append(j)
    sp += vs
    print(sp)
ans = 0

for i in alph:
    print(i, sp.count(i))
    if sp.count(i) > ans:
        ans = sp.count(i)

print(ans)
