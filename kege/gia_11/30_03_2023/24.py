f = open('files/24_6757.txt', 'r')

s = f.readline()

s = s.replace('FC', 'PP')
s = s.replace('CF', 'PP')

search = 'PPE'

while search in s:
    search = search + 'PPE'

print(len(search) // 3)