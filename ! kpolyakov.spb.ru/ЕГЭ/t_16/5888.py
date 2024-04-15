'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5888
'''

sp = []

for n in range(4965):
    if n <= 3:
        sp.append(n - 1)
    if (n > 3) and (n % 2 == 0):
        sp.append(sp[n - 2] + n // 2 - sp[n - 4])
    if (n > 3) and (n % 2 != 0):
        sp.append(sp[n - 1] * n + sp[n - 2])

print(sp[4952] + 2 * sp[4958] + sp[4964])
