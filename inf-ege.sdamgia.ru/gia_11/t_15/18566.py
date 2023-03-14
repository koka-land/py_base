'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6111
*by Aldoshin Nikita
'''


for a in range(300):
    c=0
    for n in range(300):
        for m in range(300):
            if (3*m+4*n>66)or(m<=a)or(n<a):
                c+=1
    if c==90000:
        print(a)
        break