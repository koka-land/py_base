import re
s = open('files/24_19968.txt').readline()

ans = []

for i in re.findall(r'(?:0|[1-5][0-5]*)(?:[+*](?:0|[1-5][0-5]*))+', s):
    ans.append([len(i), i])
print(max(ans, key=lambda x: x[0]))