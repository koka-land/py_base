import re

s = open('files/24_20813.txt').readline()

ans = []

for i in re.findall(r'(?:0|[7-9][07-9]*)(?:[-*](?:0|[7-9][07-9]*))*', s):
    ans.append([len(i)])
print(max(ans))