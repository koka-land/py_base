n = int(input())
ans1 = ans2 = ans3 = ans4 = ans5 = 'None'
c = 0

for i in range(n):
    a = int(input())
    if a % 10 == 5:
        if ans1 == 'None':
            ans = a
        else:
            if a > ans1:
                ans1 = a
    if a % 3 == 0:
        if ans2 == 'None':
            ans2 = a
        else:
            ans2 += a
        c += 1












    if a % 7 == 0:
        if ans3 == 'None' or a < ans3:
            ans3 = a
    if 20 < a < 50:
        if ans4 == 'None':
            ans4 = 1
        else:
            ans4 += 1
    if 100 <= abs(a) <= 999:
        if ans5 == 'None':
            ans5 = a
        else:
            ans4 += a

print(ans1)
print(ans2)
if ans3 != 'None': print(ans3 / c)
else: print(ans3)
print(ans4)
print(ans5)



