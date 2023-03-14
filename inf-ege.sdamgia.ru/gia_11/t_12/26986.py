'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6111
*by Aldoshin Nikita
'''


s='7'*40+'9'*40+'4'*50
while ('49' in s)or ('97'in s)or('47'in s):
    if ('47' in s):
        s=s.replace('47','74',1)
    if ('97' in s):
        s=s.replace('97','79',1)
    if ('49' in s):
        s=s.replace('49','94',1)
print(s[25],s[71],s[105])
