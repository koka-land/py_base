'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6099
'''

s = open('files/24-249.txt', 'r').readline()
minn = 10**10
l = 0
p = 16
f = 0
e = 0
b = '0123456789ABCDEF'

while e == 0:
    for i in b:
        if i in s[l:p:]:
            f = 0
        else:
            f = 1
            break
    if f == 0:
        minn = min(minn, p - l)
        l += 1
    else:
        if p + 1 <= len(s):
            p += 1
        else:
            e = 1

print(minn)
