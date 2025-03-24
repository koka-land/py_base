f = open('files/17_17873.txt')
sp = [int(i) for i in f]
sp_min = min(sp)
sp_ans = []

sp_ans = [sp[i] + sp[i + 1] for i in range(len(sp) - 1) if (sp[i] % 16 == sp_min) or (sp[i + 1] % 16 == sp_min)]

print(len(sp_ans), max(sp_ans))