from random import shuffle
import time

f1 = open('files/10k-sorted.txt', 'w')
f2 = open('files/10k-back_sorted', 'w')
f3 = open('files/10k-min-max-min', 'w')
f4 = open('files/10k-max-min-max', 'w')
f5 = open('files/10k-random', 'w')

n= 10001

sp1 = list(range(1, n))
sp2 = sp1[::-1]
sp3 = sp1[0::2] + sp2[0::2]
sp4 = sp2[1::2] + sp1[1::2]
sp5 = list(range(1, n))
shuffle(sp5)

sp1_1 = sp1[:]
sp1_2 = sp1[:]
sp1_3 = sp1[:]
sp2_1 = sp2[:]
sp2_2 = sp2[:]
sp2_3 = sp2[:]
sp3_1 = sp3[:]
sp3_2 = sp3[:]
sp3_3 = sp3[:]
sp4_1 = sp4[:]
sp4_2 = sp4[:]
sp4_3 = sp4[:]
sp5_1 = sp5[:]
sp5_2 = sp5[:]
sp5_3 = sp5[:]

f1.writelines(str(sp1)[1:-1:])
f2.writelines(str(sp2)[1:-1:])
f3.writelines(str(sp3)[1:-1:])
f4.writelines(str(sp4)[1:-1:])
f5.writelines(str(sp5)[1:-1:])

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

def bubble(x):
    start = time.time()
    for j in range(len(x) - 1):
        f = 0
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
                f = 1
        if f == 0:
            break
    end = time.time()
    return round(end - start, 2)

def selection_sort(x):
    start = time.time()
    i = 0
    while i < len(x) - 1:
        m = i
        j = i + 1
        while j < len(x):
            if x[j] < x[m]:
                m = j
            j += 1
        x[i], x[m] = x[m], x[i]
        i += 1
    end = time.time()
    return round(end - start, 2)

def insertion_sort(x):
    start = time.time()
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key
    end = time.time()
    return round(end - start, 2)


print('%5s %15s %15s %15s' % ('', 'Bubbles', 'Selection Sort', 'Insertion Sort'))
print('%5s %15s %15s %15s' % ('sp1', bubble(sp1_1), selection_sort(sp1_2), insertion_sort(sp1_3)))
print('%5s %15s %15s %15s' % ('sp2', bubble(sp2_1), selection_sort(sp2_2), insertion_sort(sp2_3)))
print('%5s %15s %15s %15s' % ('sp3', bubble(sp3_1), selection_sort(sp3_2), insertion_sort(sp3_3)))
print('%5s %15s %15s %15s' % ('sp4', bubble(sp4_1), selection_sort(sp4_2), insertion_sort(sp4_3)))
print('%5s %15s %15s %15s' % ('sp5', bubble(sp5_1), selection_sort(sp5_2), insertion_sort(sp5_3)))

