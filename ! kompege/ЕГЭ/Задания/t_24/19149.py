import re
s = open('files/24_19149.txt').readline()
max_len = 0

for i in re.findall(r'(?:[(])(?:[1-4]+)(?:[+](?:[1-4][1-4]*))+(?:[)])', s):
    sp = list(map(int, i[1:-1:].split('+')))
    if sum(sp) % 2 == 0:
        max_len = max(len(i), max_len)

print(max_len)