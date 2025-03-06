import re
s = open('files/24_19969.txt').readline()

ans = []

for i in re.findall(r'([a-z]+@[a-z]+.[a-z]+)', s):
    ans.append([len(i), i])
print(max(ans, key=lambda x: x[0]))