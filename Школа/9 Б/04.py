sp = [int(i) for i in input().split(' ')]
sp.insert(sp.index(max(sp)), sum([sp[i] for i in range(sp.index(max(sp))) if sp[i] > 0]))
print(sp)