s = open('files/24_8579.txt').readline()
sc = -1
sc_chet = -1
num = '0123456789'
max_str = 0
for i in range(len(s)):
    if s[i] in num:
        if sc == -1:
            sc = i
            sc_chet = int(s[i]) % 2
        else:
            if int(s[i]) % 2 == sc_chet:
                sc = i
            else:
                max_str = max(max_str, i - sc + 1)
                sc = i
                sc_chet = int(s[i]) % 2

print(max_str)


