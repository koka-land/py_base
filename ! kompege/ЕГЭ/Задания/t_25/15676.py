from fnmatch import *
for i in range(22768, 10**8 + 1, 22768):
    if fnmatch(str(i), '1*03*6*'):
        #print(i, i % 22768)
        if str(i).count('03') == 1:
            n = str(i)[1:str(i).index('03')]
            if len(n) > 0:
                f = 0
                for j in range(2, int(int(n) ** 0.5) + 1):
                    if int(n) % j == 0:
                        f = 1
                        break
                if f == 1:
                    print(i, int(n))
