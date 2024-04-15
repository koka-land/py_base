from itertools import product

count = 0
otvet = set()

for a, b, c, d in product(['0', '1', '2', '3', '4', '5', '6', '7'], repeat=4):
    s = a + b + c + d
    sp = set([a, b, c, d])
    if s[0] != '0' and len(sp) == 3:
        if s[0] == s[1] or  s[1] == s[2] or s[2] == s[3]:
            otvet.add(s)

print(len(otvet))