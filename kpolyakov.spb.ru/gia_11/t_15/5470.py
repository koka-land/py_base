'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5470
'''

#Таблица истинности

print('P Q A F')
for P in range(2):
    for Q in range(2):
        for A in range(2):
            print (P, Q, A, (P and not(A)) <= Q)

#Решение 1            
            
P = set(range(254, 801))
Q = set(range(410, 824))
A = set()
k = 0

for x in range(250, 830):
    if not(((x in P) and (x not in A)) <= (x in Q)):
        A.add(x)
        k += 1
        
print(k)

#Решение 2

c = []

def f(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

for a in range(254, 823):
    for b in range(a + 1, 824):
        if all((f(254, x, 800) and (not(f(a, x, b)))) <= f(410, x, 823) for x in range(200, 1000)):
            c.append(b - a)
            
print(min(c) + 1) #+1 пишем, потому что число x может быть нецелым, и нужно расширить отрезок на 1 точку вправо, невключая ее
