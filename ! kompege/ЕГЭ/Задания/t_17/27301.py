max45 = max(int(i) for i in open('files/17_27301.txt') if i[:2] == '45')
sp = [int(i) for i in open('files/17_27301.txt')]
triads = [[sp[j + i] for j in range(3)] for i in range(len(sp) - 2)]
ans1 = [sum(i) for i in triads if sum(1 for j in i if j < 0) == 1 and sum(i) >= max45]
ans2 = [i for i in ans1 if str(i)[-2:] == '45']
print(len(ans1))
print(min(ans2))