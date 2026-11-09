ans = []
a = int(input())
while a != 0:
    ans.append(a)
    a = int(input())
ans.sort()

print(ans[-1] + ans[-2])
print(ans[0] + ans[1])