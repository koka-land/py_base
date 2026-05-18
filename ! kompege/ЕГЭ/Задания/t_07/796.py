import math
n = 1600
i = math.ceil(math.log2(n))
I = (i * 480 * 640) / 1024 / 8
print(math.ceil(I))