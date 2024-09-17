f = open('files/24_17756.txt').readline()

f = f.replace('++', '+ +')
f = f.replace('**', '* *')
f = f.replace('*+', '* +')
f = f.replace('+*', '+ *')

res = f.split(' ')

res_max = [len(x) for x in res]
print(max(res_max))

