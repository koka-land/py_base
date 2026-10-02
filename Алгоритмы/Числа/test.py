def v3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s

def v3_r(x):
    s = ''
    while x > 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]

print(v3(91959516549684621654))
print(v3_r(91959516549684621654))
