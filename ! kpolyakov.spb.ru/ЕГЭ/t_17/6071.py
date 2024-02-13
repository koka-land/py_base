f = open('files/17-361.txt', 'r')
min_3 = 10**10
max_n = 0
count = 0

sp = list(map(int, f.readlines()))

for i in sp:
    if str(i)[-2::] == '40' and i < min_3:
        min_3 = i

for i in range(len(sp)-2):
    sp_m = [sp[i], sp[i+1], sp[i+2]]
    if (sp_m[0] == sp_m[1]) and (sp_m[1] != sp_m[2]) or (sp_m[0] != sp_m[1]) and (sp_m[1] == sp_m[2]):
        if (sp_m[0] > min_3) and (sp_m[1] > min_3) and (sp_m[2] > min_3):
            count += 1
            if 2 + i > max_n:
                max_n = 2 + i

print(count, max_n + 1)