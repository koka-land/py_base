for n in range(1,1354):
    r = oct(n)[2:]
    if r[0] == '5':
        r = '11' + r.replace('2', '*').replace('1', '2').replace('*', '1')
    else:
        r = '2' + r[1:] + '10'
    r = int(r, 8)
    if r < 1354:
        print(n, r)
