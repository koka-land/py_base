import sys
from functools import cache
sys.setrecursionlimit(15000)
def path():
    graph = {}
    with open('files/23_31673.txt') as f:
        for i in f:
            l =  i.split()
            u, v, w = int(l[0]), int(l[1]), float(l[2])
            if u not in graph:
                graph[u] = {}
            graph[u][v] = w
    w_start = graph[2691][2840]
    w_end = graph[9180][9514]
    @cache
    def dfs(c_node):
        if c_node == 9180:
            return 0
        if c_node not in graph:
            return float('inf')
        min_path = float('inf')
        for n, w in graph[c_node].items():
            dist = dfs(n)
            if dist != float('inf'):
                min_path = min(min_path, dist + w)
        return min_path
    core_path = dfs(2840)
    total_dist = w_start + core_path + w_end
    return int(total_dist)
print(path())