'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5834
'''

for n in range(10**10):
    if n % 2 == 0:
        r = hex(n)[2::] + 'f'
    else:
        r = hex(n)[2::] + '0'
    summ = 0
    for j in range(2):
        for i in r:
            summ += int(i,16)
        r += hex(summ % 16)[2::]
    if r.count(min(r)) * 5 <= r.count(max(r)):
        print(n)
        break