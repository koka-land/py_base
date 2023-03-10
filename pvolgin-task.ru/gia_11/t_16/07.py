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
    
def f(n):
    if n == 0:
        return 1
    else:
        return 7 * (n - 1) + f(n - 1)

count = 0

for i in range(1, 201):
    if prime(f(i)) == True:
        count += 1
        #print(i, f(i))

print(count)
