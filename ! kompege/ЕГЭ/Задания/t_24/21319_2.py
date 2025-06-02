def check(a):
    if int(a) < 256 and len(str(int(a))) == len(a): return True
    return False

s = open('files/24_21319.txt').readline()
ans = 0

sp = [i.split('.') for i in s.split('..') if len(i.split('.')) > 3]
for i in sp:
    for n in range(1, len(i) - 2):
        mini_sp = i[n-1:n+3]
        if check(mini_sp[1]):
            if check(mini_sp[2]):
                mini_sp[0] = mini_sp[0][-3:]
                mini_sp[3] = mini_sp[3][:3]
                for l in range(1, len(mini_sp[0]) + 1):
                    for r in range(1, len(mini_sp[3]) + 1):
                        if check(mini_sp[0][-l:]):
                            if check(mini_sp[3][:r]):
                                ans += 1

print(ans)


