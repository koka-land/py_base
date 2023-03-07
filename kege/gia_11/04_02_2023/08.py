ch = '0246'
nech = '135'
count = 0

for i1 in ch:
    for i2 in nech:
        for i3 in ch:
            for i4 in nech:
                for i5 in ch:
                    for i6 in nech:
                        num = i1 + i2 + i3 + i4 + i5 + i6
                        if num[0] != '0':
                            if num.count('6') == 1:
                                count += 1

for i1 in nech:
    for i2 in ch:
        for i3 in nech:
            for i4 in ch:
                for i5 in nech:
                    for i6 in ch:
                        num = i1 + i2 + i3 + i4 + i5 + i6
                        if num.count('6') == 1:
                            count += 1

print(count)
