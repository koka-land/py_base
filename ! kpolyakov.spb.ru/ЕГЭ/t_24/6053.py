'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6053
'''

f = open('files/24-241.txt')
s = f.readline()
start = s.index('O')
o_index = True
max_len = 0

while o_index:
    try:
        s.index('O', start + 1)
        o_start = start
        start = s.index('O', start) + 1
        o_end = start
        if s.count('F', o_start, o_end) <= 2 and o_end - o_start + 1> max_len:
            max_len = o_end - o_start + 1
    except ValueError:
        o_index = False

print(max_len)