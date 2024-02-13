from math import ceil
orders = []
num_orders = 0

v = 0
f = open('orders.txt', 'r+')
data = int(f.readline())
sklad = int(f.readline())
out = int(f.readline())
out_day = 0
production, max_product = map(int, f.readline().split(';'))
for i in f:
    orders.append(list(map(int, i.split(';'))))
num_orders = len(orders)

def menu():
    global v, sklad
    print('Дата:', data, 'день   На складе:',sklad, '     Можно выгрузить:', out - out_day)
    print('Меню')
    print('  1 - Посмотреть заказы')
    print('  2 - Удалить заказ')
    print('  3 - Добавить заказ')
    print('  4 - Сохранить и завершить')
    print()
    v = int(input('Ваш выбор: '))
    return v

def view():
    for i in orders:
        if i[3] == 0:
            print('Номер заказа:', i[0], '   Количество деталей', i[1], '   Будет готово через', i[2], 'д.')
        else:
            print('Номер заказа:', i[0], '   Количество деталей', i[1], '   Заказ выполнен!')
    print()

def delete():
    global num_orders
    for i in orders:
        print('Номер заказа:',i[0],'   Количество деталей',i[1])
    v = int(input('Выберите номер заказа для удаления: '))
    if v <= num_orders:
        orders.pop(v-1)
        print('Заказ №', v, 'успешно удален!')
        for j in range(v-1, len(orders)):
            orders[j][0] = orders[j][0] - 1
    else:
        print('Заказа №',v,'не существует!')
    num_orders = len(orders)

def create():
    global orders, sklad, production, out, out_day
    if len(orders) == 0:
        days = 0
    else:
        days = orders[-1][2]
    print('Добавление заказа')
    detali = int(input('Введите количество деталей: '))
    if len(orders) != 0:
        if orders[-1][-1] == 1:
            if detali < out - out_day:
                sklad -= detali
                out_day += detali
            else:
                sklad -= out - out_day
                out_day = out
            days = ceil((detali - (out - out_day)) / out)
        else:
            days = ceil((detali) / out) + orders[-1][-2]
    else:
        if detali < out:
            sklad -= detali
            out_day += detali
        else:
            sklad -= out
            out_day = out

        days = ceil((detali - out) / out)
    if days == 0:
        l = [len(orders) + 1, detali, days, 1]
    else:
        l = [len(orders) + 1, detali, days, 0]
    orders.append(l)

def end_day():
    global data, sklad, max_product, production
    f.truncate(0)
    f.seek(0)
    data += 1
    if orders[-1][3] == 0:
        if sklad + production - out > max_product:
            sklad = 500
        else:
            sklad += production - out
    else:
        if sklad + production > max_product:
            sklad = 500
        else:
            sklad += production
    f.write(f'{data}\n')
    f.write(f'{sklad}\n')
    f.write(f'{out}\n')
    f.write(f'{production};{max_product}\n')
    for i in orders:
        if i[2] - 1 <= 0:
            f.write(f'{i[0]};{i[1]};0;1\n')
        else:
            f.write(f'{i[0]};{i[1]};{i[2] - 1};0\n')
    f.close()


while v != 4:
    menu()
    if v == 1:
        view()
    if v == 2:
        delete()
    if v == 3:
        create()
    if v == 4:
        end_day()
        break