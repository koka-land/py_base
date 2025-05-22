import string
nos = string.ascii_uppercase[2::]

s = open('files/24_22362.txt').readline()

for i in nos:
    s = s.replace(i, ' ')

sp = [i for i in s.split(' ') if len(i) > 0]

max_len = 0
min_num = 'B' * 100

for i in sp:
    start = 0
    while i[start] == '0' and start != len(i) - 1:
        start += 1
    if len(i[start::]) >= max_len and int(i[start::], 12) % 3 == 0:
        if len(i[start::]) > max_len:
            max_len = len(i[start::])
            min_num = i[start::]
        else:
            if int(i[start::], 12) < int(min_num, 12):
                min_num = i[start::]

print(s.index(min_num))
