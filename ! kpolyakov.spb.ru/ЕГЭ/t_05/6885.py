'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6885
'''

min_r = 10 ** 100
c = '0123456789ABCDE'
def v15(n):
    r = ''
    while n > 0:
        r = c[n % 15] + r
        n //= 15
    return r

for i in range(15, 1000):
    r = v15(i)
    if i % 15 == 0:
        r = r + r[0:2]
    else:
        r = r + v15((i % 15) * 13)
    r = int(r, 15)
    if r > 700:
        min_r = min(min_r, r)

print(min_r)

