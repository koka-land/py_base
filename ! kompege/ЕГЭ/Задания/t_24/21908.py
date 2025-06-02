from re import finditer
print(max([len(i.group()) for i in finditer(r'[1-9AB][0-9AB]*[02468A]', open('files/24_21908.txt').readline())]))
