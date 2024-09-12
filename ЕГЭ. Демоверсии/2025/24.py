import re

f = open('files/demo_2025_24.txt').readline()
example = '0006789*00*789*-789*789'
res = re.findall(r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))*', example)
print(res)
res_max = [len(x) for x in res]
print(max(res_max))
print(len(res_max))

