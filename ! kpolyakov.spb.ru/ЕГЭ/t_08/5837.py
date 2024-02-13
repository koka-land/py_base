'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5837
'''

s = 'АМФИАХИЙ'
kol = []

for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    for i6 in s:
                        for i7 in s:
                            for i8 in s:
                                sl = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8
                                if sl.count('М') == 1:
                                    if sl.count('Ф') == 1:
                                        if sl.count('Х') == 1:
                                            if sl.count('Й') == 1:
                                                if sl.count('И') == 2:
                                                    if sl.count('А') == 2:
                                                        kol.append(sl)

kol = list(set(kol))
print(len(kol))
