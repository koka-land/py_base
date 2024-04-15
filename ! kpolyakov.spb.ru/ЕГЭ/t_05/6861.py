'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6861
'''

minimum = 10**30

for j in range(1001, 1500):
    sp = []
    a = j
    while a > 0:
        sp.append(a % 45)
        a = a // 45
    sp.reverse()
    s1 = 0
    for i in range(0, len(sp), 2):
        s1 += sp[i]
    s2 = sum(sp) - s1
    sp = [min(s1, s2)] + sp + [max(s1, s2)]
    print(sp)
    sp.reverse()
    otvet = 0
    for i in range(len(sp)):
        otvet = otvet + sp[i]*45**i
    if otvet < minimum:
        minimum = otvet

print(minimum)
