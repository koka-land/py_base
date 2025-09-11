import string

s = string.ascii_uppercase

print('s', s)
print('s[10::]', s[10::])
print('s[10:20:]', s[10:20:])
print('s[10:20:2]', s[10:20:2])
print('s[-10::]', s[-10::])
print('s[-10:-5:]', s[-10:-5:])
print('s[::-1]', s[::-1])