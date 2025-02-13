import re
s = open('files/24_19970.txt').readline()

ans = []

for i in re.findall(r'(?:0|[1-9][0-9]*[05])(?:[+*](?:0|[1-9][0-9]*[05]))+', s):
    ans.append([len(i), i])
print(max(ans, key=lambda x: x[0]))
