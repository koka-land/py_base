s = open('files/24_14704.txt').readline()

s1 = s[0]
vv = 1
otvet = 0

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        s1 += s[i]
    if s[i] > s[i - 1]:
        if vv == 2:
            otvet = max(otvet, len(s1))
            s1 = s[i - 1]
            vv = 1
        s1 += s[i]
        vv = 1
    elif s[i] < s[i - 1]:
        s1 += s[i]
        vv = 2

print(otvet)