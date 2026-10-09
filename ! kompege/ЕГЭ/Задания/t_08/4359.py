from itertools import product

#1 способ - "в лоб"
s = 'АИКЛМЬ'
w = []
for i in product(s, repeat=6):
    w.append(''.join(i))
for i in range(len(w)):
    if w[i][0] == 'К':
        if w[i][-1] == 'Ь':
            if len(set(w[i])) == 6:
                if w[i + 26655][::-1] == w[i]:
                    print(sum(int(x) for x in str(i + 1)))
                    break

#2 способ через 6-ую систему счисления в 1 строку
print([sum(int(i) for i in str(int(i, 6))) + 1 for i in (i for i in (''.join(i) for i in product('012345', repeat=6)) if i[0] == '2' and i[-1] == '5' and len(set(i)) == len(i)) if int(i, 6) + 26655 == int(i[::-1], 6)][0])

#3 способ, не в одну строку =)
for i in product('012345', repeat=6):
    n = ''.join(i)
    if n[0] == '2' and n[-1] == '5' and len(n) == len(set(n)):
        if int(n, 6) + 26655 == int(n[::-1], 6):
            print(sum(int(i) for i in str(int(n, 6) + 1)))
            break