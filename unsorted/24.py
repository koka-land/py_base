f = open('24_3.txt')
s = f.readline()
i = s.index('A')
count = 0
while i < len(s) - 12:
    if s[i+11] == 'A':
        if (s[i+1:i+10].count('A') == 0) and (s[i+1:i+10].count('B') == 0):
            count += 1
        i = i+11
    else:
        i = s.index('A', i+1)
print(count)