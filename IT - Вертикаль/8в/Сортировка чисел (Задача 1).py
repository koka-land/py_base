#Создать списко из 30 чисел (15 четныз, 15 нечетных)
#Отсортировать числа: четные в порядке возрастания, затем нечетные в порядке убывания

from random import randint
nums = []
nums_ch = []
nums_nech = []

while len(nums_ch) != 15 or len(nums_nech) != 15:
    a = randint(1, 1000)
    if a % 2 == 0 and len(nums_ch) < 15:
        nums_ch.append(a)
    else:
        if len(nums_nech) < 15:
            nums_nech.append(a)

nums_ch.sort()
nums_nech.sort(reverse=True)
nums = nums_ch + nums_nech
print(nums)