from math import ceil

f = open('files/27A_15342.txt')
k, l = map(int, f.readline().split())
sp = []

for i in f:
	sp.append(list(map(int, i.split())))
	sp[-1][1] = ceil(sp[-1][1] / 11)

mincost = 10 ** 10

for i in range(k):
	cost = 0
	s = (sp[0][0] + l // 2) % l
	for j in range(1, k):
		if sp[j][0] >= min(sp[0][0], s) and sp[j][0] <= max(sp[0][0], s):
			cost += abs(sp[0][0] - sp[j][0]) * sp[j][1]
		else:
			if abs(sp[0][0] - sp[j][0]) < (l // 2):
				cost += abs(sp[j][0] - sp[0][0]) * sp[j][1]
			else:
				cost += abs(l - sp[0][0] + sp[j][0]) * sp[j][1]

	mincost = min(mincost, cost)
	sp.append(sp[0])
	sp.pop(0)

print(mincost)
