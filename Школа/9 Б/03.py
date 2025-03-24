s = input()
sp = [i for i in s.split(' ') if i[-1] == 'e']
print(s.replace(min(sp, key=len) + ' ', ''))
