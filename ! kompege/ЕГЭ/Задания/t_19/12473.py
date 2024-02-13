def F(S, m):
    if S == 128:
        return m%2 == 0
    if S > 128:
        return m%2 == 1
    if m == 0:
        return False
    array = [F(S+1, m-1), F(S*2, m-1)]
    if m%2 == 1:
        return any(array)
    else:
        return all(array)

print(min([S for S in range(1, 129) if not F(S, 0) and F(S, 2)]))
a20 = [S for S in range(1, 129) if not F(S, 1) and F(S, 3)]
print(a20[0], a20[1])
print(len([S for S in range(1, 129) if not F(S, 0) and F(S, 2)]))
