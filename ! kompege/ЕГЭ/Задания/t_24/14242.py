s = open('files/24_14242.txt').readline()
s = s.replace('2', '0')
s = s.replace('3', '1')
s = s.replace('D', 'B')
s = s.replace('E', 'A')

max_str = 0

for sc in range(len(s) - 3):
    for ec in range(sc + 4, len(s) + 1):
        if s[sc:ec].count('0') == \
           s[sc:ec].count('1') == \
           s[sc:ec].count('A') == \
           s[sc:ec].count('B'):
            max_str = max(max_str, ec - sc)

print(max_str)
