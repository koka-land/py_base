ans = []
n = int(input())
for i in range(n):
    a = int(input())
    if a % 10 == 6:
        ans.append(a)
print(min(ans))
