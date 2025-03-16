'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5915
'''

s = '1' * 33 + '2' * 33

while '11' in s or '22' in s or '13' in s or '23' in s:
    s = s.replace('11', '2', 1)
    s = s.replace('22', '1', 1)
    s = s.replace('13', '2', 1)
    s = s.replace('23', '1', 1)

print(sum([int (i) for i in s]))
print(s)

#В исходную строку нужно добавить одну "3", для того чтобы сумма цифр конечной строки была наименьшей:
#Исходная строка: 111...1113222...222
#В этом случае конечная строка будет состоять из одной "1"

