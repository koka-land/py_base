ans = []
for i in range(1000, 10000):
    n = sorted([int(str(i)[0]) * int(str(i)[1]), int(str(i)[1]) * int(str(i)[2]), int(str(i)[2]) * int(str(i)[3])])
    if len(str(int((str(n[0]) + str(n[1]) + str(n[2]))))) == 4:
        ans.append(int(str(n[0]) + str(n[1]) + str(n[2])))
print(len(ans))
print(ans)