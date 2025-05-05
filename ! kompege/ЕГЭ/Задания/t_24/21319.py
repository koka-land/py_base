s = open('files/24_21319.txt').readline()
t = '.'
while t in s:
    if t + '.' in s:
        t += '.'
    else:
        break
while len(t) > 1:
    s = s.replace(t, ' ')
    t = '.' * (len(t) - 1)

sp = s.split(' ')
ans = []

for i in sp:
    a_sp = i.split('.')
    if len(a_sp) > 3:
        for j in range(len(a_sp) - 3):
            good = 0
            for k in range(1, 3):
                if a_sp[j + k][0] == '0' and len(a_sp[j + k]) > 1 or int(a_sp[j + k]) > 255:
                    break
                else:
                    good += 1
            if good == 2:
                n = []
                k = []
                ip = [a_sp[j][-3:], a_sp[j + 1], a_sp[j + 2], a_sp[j + 3][:3]]
                while len(ip[0]) < 3:
                    ip[0] = '0' + ip[0]
                if 99 < int(ip[0]) < 256:
                    n.append(ip[0])
                if 9 < int(ip[0][1:]) < 100:
                    n.append(ip[0][1:])
                if int(ip[0][2:]) < 10:
                    n.append(ip[0][2:])
                if 99 < int(ip[3]) < 256:
                    k.append(ip[3])
                if 9 < int(ip[3][:2]) < 100:
                    k.append(ip[3][:2])
                if int(ip[3][:1]) < 10:
                    k.append(ip[3][:1])
                for j1 in n:
                    for j2 in k:
                        ans.append(j1+'.'+ip[1]+'.'+ip[2]+'.'+j2)
print(len(ans))
