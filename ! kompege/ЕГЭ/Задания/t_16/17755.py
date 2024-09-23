sp = [0] * 413

for i in range(412, 71, -1):
    if i > 400:
        sp[i] = i ** i
    else:
        sp[i] = i + 6 + sp[i + 12]

print(sp[72] - sp[108])