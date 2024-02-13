f = open('files/27_B_8513.txt')
k = int(f.readline())
n = int(f.readline())
sp = []
# Полуручной способ через нахождение индексов максимальных чисел
# sp1 = []
# for i in f:
#     sp.append(int(i))
#     sp1.append(int(i))
# print(len(sp))
# sp1.sort(reverse=True)
# print(sp1[0:10])
# print(sp.index(1045460))
# print(sp.index(1045460,820400 + 1))
# pos = 0
# for i in range(sp1.count(1045460)):
#     print(sp.index(1045460, pos), end=' ')
#     pos = sp.index(1045460, pos) + 1
# print()
# pos = 0
# for i in range(sp1.count(1045459)):
#     print(sp.index(1045459, pos), end=' ')
#     pos = sp.index(1045459, pos) + 1
# print()
# print(max(sp)+max(sp))

# Автоматический способ
for i in range(k):
    sp.append(int(f.readline()))
max_do = 0
max_sum = 0
for i in range(n - k):
    a = int(f.readline())
    max_sum = max(a + sp[i], max_sum, a + max_do)
    max_do = max(max_do, sp[i])
    sp.append(a)
print(max_sum)