'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6147
'''

s = open('files/24-250.txt', 'r').readline()
start = end = s.index('.')
a = 1
minn = 10**10

for i in range(6):
    end = s.index('.', end + 1)

while a:
    try:
        s.index('.', end + 1)
        start = s.index('.', start + 1)
        end = s.index('.', end + 1)
        minn = min(minn, end - start + 1)
    except ValueError:
        a = 0

print(minn)