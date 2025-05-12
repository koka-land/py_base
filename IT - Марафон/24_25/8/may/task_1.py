def e():
    print('ERROR')

def troubleshooting(name, age):
    if all(i.isalpha() for i in name):
        if name[0].isupper() and all(i.islower() for i in name[1:]):
            if all(i.isdigit() for i in age):
                if 49 < int(age) < 251:
                    return False
    return True

s = input()

if '  ' in s or len(s.split(' ')) % 2 != 0 or '' in s.split(' '):
    e()
else:
    table = [[s.split()[i], s.split()[i + 1]] for i in range(0, len(s.split()), 2)]
    for i in table:
        if troubleshooting(i[0], i[1]):
            e()
            exit()

    table = sorted(table, key=lambda x: x[1], reverse=True)

    for i in table:
        print(i[0], i[1])

