import string

sym = string.digits + string.ascii_uppercase

a = int('SLADOST', 36)
b = 'GADOST'[::-1]
c = 'HALLOWEEN'[::-1]
d = 166729861760449

for x in range(10):
    b_dec = 0
    c_dec = 0
    i = 0
    for c_ in b:
        b_dec += sym.index(c_) * (int(f'10{x}') ** i)
        i += 1
    i = 0
    for c_ in c:
        c_dec += sym.index(c_) * ((50 - x) ** i)
        i += 1
    if (a + b_dec) == (c_dec - d):
        print(x)
        break

i = 0
ans = 0
for c_ in b:
    ans += sym.index(c_) * (int(f'{x}13') ** i)
    i += 1

print(ans)
