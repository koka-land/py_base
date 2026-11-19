kl = [[], [], [], []]
f = open('files/4416.csv')
for i in f:
    s = i.split(';')
    e = float(s[4]) * 0.5 * (float(s[2])**2 + float(s[3])**2)
    s = list(map(float, s[:5])) + [e] +  [int(s[6])] + [s[7][:-1]]
    if s[6] == 1:
        kl[0].append(s)
    elif s[6] == 2:
        kl[1].append(s)
    elif s[6] == 3:
        kl[2].append(s)
    else:
        kl[3].append(s)

c_kl = [[], [], [], []]
p2 = [[], [], [], []]

for i in range(4):
    min_s = 10**10
    for chast_alpha in kl[i]:
        if chast_alpha[7] == 'II':
            p2[i].append(chast_alpha)
        s_ = 0
        for chast in kl[i]:
            s_ += abs(chast_alpha[5] - chast[5])
        if s_ < min_s:
            c_kl[i] = chast_alpha
            min_s = s_

max_s = 0
for i in range(4):
    for chast_alpha in p2[i]:
        for chast in p2[i]:
            s_ = ((chast[0] - chast_alpha[0])**2 + (chast[1] - chast_alpha[1])**2)**0.5
            if s_ > max_s:
                max_s = s_

print('Q1', int(max_s*10000))
print('Q2', int(max(c_kl[0][5], c_kl[1][5], c_kl[2][5], c_kl[3][5])*10000))