incorrect_input = True
sym_change = 'OIZE!SbJ#P'
new_pass = ''

while incorrect_input:
    num = input()
    try:
        int(num)
    except ValueError:
        print('Вы ввели не число')
    else:
        if int(num) not in range(10**6, 10**7):
            print('Вы ввели не семизначное число')
        else:
            incorrect_input = False
            num = str(int(num))

num = (num + num[0])[::-1]
for i in num:
    new_pass += sym_change[int(i)]

print(num, new_pass)

