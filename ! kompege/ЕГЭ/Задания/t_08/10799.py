s1 = 'КРБЛК'
s2 = 'ОАИ'
ans = set()

for c1 in s1:
    for c2 in s2:
        for c3 in s1:
            for c4 in s2:
                for c5 in s1:
                    for c6 in s2:
                        s = c1 + c2 + c3 + c4 + c5 + c6
                        mn = set(s)
                        if len(mn) == len(s):
                            ans.add(s)
                            print(s)

print(len(ans))