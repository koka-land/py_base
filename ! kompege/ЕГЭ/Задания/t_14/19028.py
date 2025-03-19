sp16 = [int('1000A00', 16), int('FFFFAFF', 16)]
sp8 = [int('100020003', 8), int('777727773', 8)]
ans = 0
print(sp16, sp8)
for i in range(max(sp16[0], sp8[0]), min(sp16[1], sp8[1]) + 1):
    if i % 8 == 3:
        if i // (8 ** 4) % 8 == 2:
            if i // 16 ** 2 % 16 == 10:
                ans += 1

print(ans)