n = int(input())
ans1 = 0
c1 = 0
ans2 = 0

for i in range(n):
    a = int(input())
    if a % 3 == 0 and a % 2 == 0:
        ans1 = ans1 + a
        c1 = c1 + 1
    if a % 5 == 0 and a > ans2:
        ans2 = a

if ans1 != 0 and ans2 != 0:
    print(ans1 // c1 + ans2)
else:
    print('НЕТ')