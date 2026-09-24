from math import *

i = ceil(log2(10000000))
max_pixels = -10
for pixels in range(1, 10**10):
    time = (pixels * i  * 10) / 2100000
    if time <= 180:
        max_pixels = pixels
    else:
        break
print(max_pixels)