'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5091
'''

sp = set()

def f(x, p):
    if p == 17:
        sp.add(x)
    else:
        f(x - 1, p + 1)
        f(x - 2, p + 1)
        if x > 0 and x**0.5 == int(x**0.5):
            f(x**0.5, p + 1)

f(113, 0)

print(len(sp))
