n = int(input())

sr_t = 0
days = 0

for i in range(n):
    t = int(input())
    if t > 0:
        sr_t += t
        days += 1

sr_t = sr_t / days

print(sr_t)
print(days)