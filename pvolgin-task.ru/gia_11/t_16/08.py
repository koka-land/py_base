def prime(x):
    f = 0
    for i in range(2, int(x**(1/2)) + 1):
        if x % i == 0:
            f = 1
            break
    if f == 0:
        return True
    else:
        return False

def sum_num(x):
    return sum(map(int, str(x)))

def f(n):
    if n <= 1:
        return 1
    if (n % 2 == 0) and (n > 1):
        return 11 * n + f(n - 1)
    if (n % 2 == 1) and (n > 1):
        return f(n - 2) * 11 + n

count = 0

for i in range(2, 36):
    №print(i, f(i), sum_num(f(i)), prime(sum_num(f(i))))
    if prime(sum_num(f(i))):
        count += 1

print(count)
