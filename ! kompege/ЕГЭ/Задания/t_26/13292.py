f = open('files/26_13292.txt')
n, k = map(int, f.readline().split())
sp = []

for i in f:
    sp.append(int(i))

sp.sort()
sklad = [0] * k
n_ch = 0
n_nech = len(sklad) - 1
n_posl = 0

for i in range(k):
    if sp[i] % 2 == 0:
        sklad[n_ch] = sp[i]
        n_posl = n_ch
        n_ch += 1
    else:
        sklad[n_nech] = sp[i]
        n_posl = n_nech
        n_nech -= 1

print(n_posl + 1, sum(sklad[n_posl + 1:]))

