s = open('files/24_26551.txt').readline()
nech = '13579BD'
import string

for i in string.ascii_uppercase[4:]:
    s = s.replace(i, ' ')
s = s.split(' ')

ans = 0

for i in s:
    if len(i) != 0:
        start = 0
        for j in range(len(i)):
            if i[j] == '0':
                start += 1
            else:
                break
        end = len(i)
        for j in range(len(i) -1, -1, -1):
            if i[j] in nech:
                end -= 1
            else:
                break
        ans = max(len(i[start:end]), ans)

print(ans)