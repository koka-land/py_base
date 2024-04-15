f = open('files/24.txt', 'r')
s = f.readline()
search = "BBA"

s.replace('C', 'B')

while search in s:
    search = search + 'BBA'

print(search)
print(len(search))
