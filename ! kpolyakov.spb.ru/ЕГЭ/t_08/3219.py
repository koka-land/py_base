'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3219
'''

s = 'КЛЕЙ'
count=0

for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    for i6 in s:
                        o = i1+i2+i3+i4+i5+i6
                        if (o[0] != 'Й') and ('ЕЙ' not in o) and ('ЙЕ' not in o) and (o[5] != 'Й') and (o.count('Й') <= 1):
                            count += 1

print(count)                                            
                        
