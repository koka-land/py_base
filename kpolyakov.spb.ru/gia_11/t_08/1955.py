'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=1955
'''

s = 'МАГИСТР'
count=0

for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    o = i1+i2+i3+i4+i5
                    if o.count('М') <= 1:
                        if o.count('Г') <= 1:
                            if o.count('С') <= 1:
                                if o.count('Т') <= 1:
                                    if o.count('Р') <= 1:
                                        if o.count('А') + o.count('И') <= 1:
                                            count += 1

print(count)                                            

