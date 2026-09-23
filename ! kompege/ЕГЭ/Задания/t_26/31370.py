f = open('files/26_31370.txt')
k, n = map(int, f.readline().split())
abonents = dict()
memory = 0
backup = []
for i in f:
    time, abonent, kb = i.split()
    time, abonent, kb = list(map(int, time.split(':'))), int(abonent), int(kb)
    abonents[abonent] = abonents.get(abonent, 0) + kb
    if time[0] < 12:
        if memory + kb <= n:
            memory += kb
        else:
            backup.append(memory)
            memory = kb
abonents = dict(sorted(abonents.items(), key=lambda x: x[1]))
print(sum(list(abonents.keys())[:2]))
print(backup[-1] + backup[-2])