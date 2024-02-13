'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6752
*by Kuzmin Andrei
'''

import sys

sys.setrecursionlimit(10000)
def f(n):
    if n >= 2022:
        return n
    elif n < 2022:
        return f(n + 5) + 7

print(f(45) - f(49))