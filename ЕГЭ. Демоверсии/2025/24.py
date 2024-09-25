import re

f = open('files/demo_2025_24.txt').readline()
res = re.findall(r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))+', f)
res_max = [len(x) for x in res]
print(max(res_max))
