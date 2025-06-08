import re

s = open('files/24_20968.txt').readline()

ans = []

for i in re.findall(r'(?:[0]|[1-9][0-9]*[02468])(?:[+*](?:[0]|[1-9][0-9]*[02468]))+', s):
    ans.append([len(i)])

print(max(ans))
