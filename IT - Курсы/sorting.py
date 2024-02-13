import random
import time
import operator

def bubble(x):
    for j in range(len(x) - 1):
        f = 0
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
                f = 1
        if f == 0:
            break
    return x

def selection_sort(x):
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
    return x

def insertion_sort(x):
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key
    return x

def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def list_create(x):
    list = []
    for i in range(x):
        list.append(random.randint(1, 10001))
    return list