a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
print('Выберите действие:')
print('  + (Сложение):')
print('  - (Вычитание):')
print('  * (Умножение):')
print('  / (Деление):')
v = input('Ваш выбор: ')
if v == '+':
    o = a + b
elif v == '-':
    o = a - b
elif v == '*':
    o = a * b
elif v == '/':
    o = a / b
else:
    print('Такого действия нет!')
op = ['+', '-', '*', '/']
if v in op:
    print('Ответ:', o)
