from math import cos, sin

x = 2
y = 2
r = 1

for a in range(0, 181, 10):
    x1 = x + r * round(cos(a), 2)
    y1 = y + r * round(sin(a), 2)
    print(str(x1).replace('.',','), str(y1).replace('.',','))
