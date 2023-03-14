'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6111
*by Aldoshin Nikita
'''


s='9'*127
while ('333'in s) or ('999'in s):
    if ('333'in s):
        s=s.replace('333','9',1)
    else:
        s=s.replace('999','3',1)
print(s)