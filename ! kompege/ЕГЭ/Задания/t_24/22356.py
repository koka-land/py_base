from re import finditer
s = open('files/24_22356.txt').readline()
a = max([[int(str(i.group()), 12), str(i.group())] for i in finditer(r'[1-9AB][0-9AB]*[13579B]', s)])
print(s.index(a[1]))