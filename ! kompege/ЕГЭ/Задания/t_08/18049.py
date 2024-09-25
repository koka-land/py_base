from itertools import product
ans = 0
#t = ['000', '111', '222', '333', '444', '555', '666', '777', '888']

for i in product('012345678', repeat=7):
    s = ''.join(i)
    if (s[0] not in '0246') and not (s[-1] == s[-2] and s[-2] == s[-3]):
    #if (s[0] not in '0246') and (s[-3:] not in t):
        ans += 1

print(ans)
