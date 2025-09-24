import sys
sys.set_int_max_str_digits(50000)

for p in range (18, 100):
    a = 2 * p**5 +  2 * p**4 + 10 * p**3 + 1 * p**2 + 2 * p + 14
    b = 2 * p**5 + 15 * p**4 +  1 * p**3 + 3 * p**2 + 9 * p + 1
    c = 1 * p**5 + 17 * p**4 +  0 * p**3 + 5 * p**2 + 13 * p + 0
    if (a + b - c) % 19 == 0:
        print((a + b - c) // 19)
        break
a = 2187**2020 - 2187**2010
print(a)
