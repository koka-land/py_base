import math
n = 12 + 31415
i = math.ceil(math.log2(n))
a = math.ceil((i * 1000) / 8)
I = (8192 * a) / 1024
print(int(I))