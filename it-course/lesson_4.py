import sorting
import time


for i in range(25, 1500, 50):
    sp1 = sorting.list_create(i)
    sp2 = sorting.list_create(i)
    sp3 = sorting.list_create(i)
    sp4 = sorting.list_create(i)
    sp5 = sorting.list_create(i)
    s1 = time.time()
    sorting.bubble(sp1)
    e1 = time.time()
    s2 = time.time()
    sorting.selection_sort(sp2)
    e2 = time.time()
    s3 = time.time()
    sorting.insertion_sort(sp3)
    e3 = time.time()
    s4 = time.time()
    sorting.merge_sort(sp4)
    e4 = time.time()
    s5 = time.time()
    sp5.sort()
    e5 = time.time()
    print('%7s %7s %7s %7s %7s' % ((round(e1 - s1, 4), round(e2 - s2, 4), round(e3 - s3, 4), round(e4 - s4, 4), round(e5 - s5, 4))))