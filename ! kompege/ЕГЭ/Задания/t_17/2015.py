f = open('files/17_2015.txt')
ans = []


for i in f:
    a = int(i)
    if (a % 10 == 5 or a % 10 == 7) and int(i) % 9 != 0 and int(i) % 11 != 0:
        ans.append(int(i))

print(len(ans), min(ans) + max(ans))
