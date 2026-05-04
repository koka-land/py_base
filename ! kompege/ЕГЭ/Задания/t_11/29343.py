import math
i = math.ceil(math.log2(4080 + 17))
print(i)
a = math.ceil(257 * i / 8)
print(a)
b = (8388608 * a) / (1024**2)
print(b)