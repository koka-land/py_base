'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6094
'''

f = open('files/26-103.txt', 'r')
n = 10000
k = 20
m = 15
sp = []
max15 = 0
c = 0

for i in f:
  sp.append(i.split())

for i in range(n):
  sp[i][0] = int(sp[i][0])
  
sp.sort(reverse=True)

while len(sp) != 0:
  c += 1
  tr = sp[0][0]
  tc = sp[0][1]
  cb = 1
  sp[0] = 0

  for i in range(1, len(sp)):
    if sp[i][0] + k <= tr:
      if sp[i][1] != tc:
        cb += 1
        tr = sp[i][0]
        tc = sp[i][1]
        sp[i] = 0
    if cb == m:
      max15 += 1
      break
  while 0 in sp:
    sp.remove(0)

print(c, max15)
