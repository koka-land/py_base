import fnmatch

for i in range(9874, 10**10 + 1, 9874):
    if fnmatch.fnmatch(str(i), r'89*6?7?9?'):
        print(i, i // 9874)