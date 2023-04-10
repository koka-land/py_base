'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6152
'''

for start in range(63233530, 10**10):
    if start % 28 == 0:
        break

for i in range(start, 10**9, 28):
    s = str(i)
    if s[0:4] == '6323' and s[-4:-1] == '353':
        print(i, i // 28)
        