s = open('files/24_18186.txt').readline()
s = s.replace('E', 'A').replace('C', 'B').replace('D', 'B').replace('F', 'B').replace('G', 'B').replace('H', 'B')
s = s[s.index('BBA'): s.rindex('BBA') + 3]
sp = s.split('BBA')

max_len = 0

for i in sp:
    max_len = max(max_len, len(i))

print(max_len + 6)