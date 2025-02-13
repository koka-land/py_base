sp = [13] * 13

for i in range(13, 3014):
    if i % 5 == 0:
        sp.append(13 + sp[i - 1])
    else:
        sp.append(13 - sp[i - 1])

print(sp[3013])