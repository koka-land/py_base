f = open('files/17_23901.txt')
count = 0
sum_ = 0

sp = [int(i) for i in f]

for i in range(len(sp) - 1):
    if (int(sp[i] % 80 == 17) + int(sp[i + 1] % 80 == 17)) == 1:
        if sp[i] % 7 == 0 and sp[i + 1] % 7 == 0:
            count += 1
            if sp[i] % 80 == 17:
                sum_ += sp[i]
            else:
                sum_ += sp[i + 1]

print(count, sum_)
