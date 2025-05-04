s = open('files/24_21319.txt').readline().replace('..', ' ')

ans = []

sp = [i.split('.') for i in s.split(' ') if len(i.split('.')) > 3]
for i in sp:
    for n in range(1, len(i) - 2):
        mini_sp = i[n-1:n+3]
        if int(mini_sp[1]) < 256 and len(str(int(mini_sp[1]))) == len(mini_sp[1]):
            if int(mini_sp[2]) < 256 and len(str(int(mini_sp[2]))) == len(mini_sp[2]):
                mini_sp[0] = mini_sp[0][-3:]
                mini_sp[3] = mini_sp[3][:3]
                for l in range(1, len(mini_sp[0]) + 1):
                    for r in range(1, len(mini_sp[3]) + 1):
                        if int(mini_sp[0][-l:]) < 256 and len(str(int(mini_sp[0][-l:]))) == len(mini_sp[0][-l:]):
                            if int(mini_sp[3][:r]) < 256 and len(str(int(mini_sp[3][:r]))) == len(mini_sp[3][:r]):
                                ans.append([mini_sp[0][-l:], mini_sp[1], mini_sp[2], mini_sp[3][:r]])

print(len(ans))


