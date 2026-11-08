f = open('files/9_3757.csv')
ans = 0
for i in f:
    ans += 1
    sp = list(map(int, i.split(',')))
    set_sp = set(sp)
    if len(sp) == len(set_sp):
        sp.sort()
        if sp[-1] - sp[0] == sum(sp[1:4]):
            print(ans)
            break