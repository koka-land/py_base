'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5787
'''

def f(x, y, turn):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        if turn != 0:
            return f(x + turn, y, x) + f(x + 1, y, x) + f(x * 3, y, x)
        else:
            return f(x + 1, y, x) + f(x * 3, y, x)

print(f(2, 27, 0))