'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6811
'''

def v3(x):
    s = '012'
    res = ''
    while x > 0:
        res = s[x % 3] + res
        x //= 3
    return res

maxn = 0

for n in range(1, 200):
    r = v3(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + v3((n % 3) * 4)
    r = int(r, 3)
    if r < 199 and n > maxn:
        maxn = n
print(maxn)




