s = open('files/24_20909.txt').readline()

ab = []
start = 0

for i in range(s.count('AB')):
    ab.append(s.index('AB', start))
    start = s.index('AB', start) + 1

max_len_ab = 0

for l in range(len(ab) - 101):
    max_len_ab = max(max_len_ab, len(s[ab[l] + 1:ab[l + 101] + 1]))

print(max(ab[100] + 1, max_len_ab, len(s) - ab[-101] + 1))
