ans = 0
n = int(input())

for i in range(n):
    a = int(input())
    if a % 7 == 1:
        ans += a

print(ans)