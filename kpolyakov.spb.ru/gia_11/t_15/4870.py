'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4870
'''

#Таблица истинности

print('P Q A F')
for P in range(2):
    for Q in range(2):
        for A in range(2):
            print (P, Q, A, (not(A) <= (not(P))) <= (A <= Q))

#Решение
            
def F(a, b, x):
    if a <= x <= b:
        return True
    else:
        return False

mn = 10**10

c = []

for a in  range(25, 50):
    for b in  range(a+1, 51):
        if all((not(F(a, b, x)) <= (not(F(25, 50, x)))) <= (F(a, b, x) <= F(32, 47, x)) for x in range(1, 100)):
            c.append(b - a)
            
print(max(c))
