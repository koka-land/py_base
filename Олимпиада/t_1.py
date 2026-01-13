s = '2357'
a = b = int(input())
num = '1'
for i in s:
    while a % int(i) == 0:
        num += i
        a //= int(i)
print(num)
num = num[::-1]
pr = 1
for i in num:
    pr *= int(i)
print(b, pr, num)
if pr == b:
    if '3332222222' in num:
        num = num.replace('3332222222', '96842', 1)
    if '3332222' in num:
        num = num.replace('3332222', '9382', 1)
    if '332222' in num:
        num = num.replace('332222', '3642', 1)
    if '33' in num:
        num = num.replace('33', '9', 1)
    if '32' in num and num.count('2') == 22:
        num = num.replace('32', '6', 1)
    if '222' in num and num.count('2') != 3:
        num = num.replace('222', '8', 1)
    if '22' in num:
        num = num.replace('22', '4', 1)
    num = sorted(list(num))
    num = ''.join(num)[::-1]
    print(num)
    if len(set(num)) == len(num):
        print(num)
    else:
        print(-1)
else:
    print(-1)