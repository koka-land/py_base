'''
https://inf-ege.sdamgia.ru/problem?id=9365
'''

s = '8' * 68

while ('222' in s) or ('888' in s):
    if '222' in s:
        s = s.replace('222', '8', 1)
    else:
        s = s.replace('888', '2', 1)

print(s)