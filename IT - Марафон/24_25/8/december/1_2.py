sym_change = 'OIZE!SbJ#P'
new_pass = ''

num = input()
if num.isdigit():
    if int(num) in range(10**6, 10**7):
        num = (num + num[0])[::-1]
        for i in num:
            new_pass += sym_change[int(i)]
        print(new_pass)
    else:
        print('WRONG')
else:
    print('WRONG')

