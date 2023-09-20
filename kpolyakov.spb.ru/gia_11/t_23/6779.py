'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6779
*by Kuzmin Andrei
'''

def f(st,fin):
    if st == fin:
        return 1
    elif st < fin:
        return 0
    elif (st == 9):
        return 0
    elif (st == 16):
        return 0
    else:
        return f(st - 1, fin) + f(st - 2, fin) + f(st // 3, fin)

print(f(19, 3))