sp = set()
ch = '02468'

for n in range(123455, 987654322):
    r = n
    for j in range(3):
        count_ch = 0
        r = str(r)
        for i in r:
            if i in ch:
                count_ch += 1
        if count_ch > len(r) - count_ch:
            r = bin(int(r))[2::] + '1'
        elif count_ch < len(r) - count_ch:
            r = bin(int(r))[2::] + '0'
        else:
            if int(r) % 2 == 0:
                r = bin(int(r))[2::] + '0'
            else:
                r = bin(int(r))[2::] + '1'
        r = int(r, 2)
    sp.add(r)

print(len(sp))