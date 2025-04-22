from fnmatch import *

for i in range(7423, 10**10 + 1, 7423):
    if fnmatch(str(i), '4*4736*1'):
        print(i, i // 7423)