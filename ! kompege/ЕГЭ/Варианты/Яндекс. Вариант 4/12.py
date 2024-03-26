sp = set()

for i in range(4, 1000):
    s = '4' + '9' * i

    while '44' in s or '9299' in s or '49' in s:
        s = s.replace('49', '944', 1)
        s = s.replace('44', '2', 1)
        s = s.replace('9299', '4', 1)
    sp.add(s)

print(len(sp))