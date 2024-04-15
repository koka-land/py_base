f = open('files/24_6636.txt', 'r')
s = f.readline()

s = s.replace('3', '1')
s = s.replace('5', '1')
s = s.replace('4', '2')

search = '21'

while search in s:
    search = search + '21'

print(len(search) - 2)