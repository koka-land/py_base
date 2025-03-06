a = input()
print(''.join(sorted([i for i in a if int(i) % 2 != 0]) + sorted([i for i in a if int(i) % 2 == 0], reverse=True)))

ans = ''
for i in range(1, 10, 2):
    ans += str(i) * a.count(str(i))
for i in range(8, -1, -2):
    ans += str(i) * a.count(str(i))
print(ans)




ch = [1, 3, 3, 2, 4, 2, 43, 234]
ch.sort(reverse=True)
print(ch)






