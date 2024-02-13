'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6063
'''
def f(x, y):
    if x > y or str(x).count('5') > 0:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 3, y) + f(x * 3, y)

print(f(1, 49))