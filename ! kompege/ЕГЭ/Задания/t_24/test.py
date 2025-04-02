s = '2+2*2+2*100' * 1000
print(eval(s))
sp = s.split('+')

for i in range(len(sp)):
    sp[i] = int(eval(sp[i]))

print(sum(sp))