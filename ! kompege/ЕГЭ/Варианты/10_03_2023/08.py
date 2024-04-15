from itertools import product

count = 0
num = 0

for i in product('АЙКОС', repeat=5):
    count += 1
    s = ''.join(i)
    if 'СС' not in s and (s.count('О') <= 1):
        num = count

print(num)