ans = 0
s = open('files/24_25361.txt').readline()
s = s.replace('2', '0').replace('4','0').replace('6', '0').replace('8', '0')
s = s.split('0')
for i in s:
    if i.count('F') >= 76:
        print(i)
        sp = []
        start = 0
        for j in range(i.count('F')):
            sp.append(i.index('F', start))
            start = i.index('F', start) + 1
        ans = max(sp[76] + 1, ans)

print(ans)
