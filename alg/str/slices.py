import string

s = string.ascii_uppercase

print(s)
print(s[10::])
print(s[10:20:])
print(s[10:20:2])
print(s[-10::])
print(s[-10:-5:])

for a in range(2):
    for p in range(2):
        for q in range(2):
            print((not(a)) <= ((p and q) <= a))