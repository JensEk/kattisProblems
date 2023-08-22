# Problem: https://open.kattis.com/problems/conquest
# By: Jens Ekenblad
# Date: 2023-06-13


import sys

# DFS from island 1 to all its neighbours and increment the spanningNation army size if neighbour is smaller
def dfs(node, graph, visited, armySizes, spanningSize):
    visited[node] = True
    spanningSize += armySizes[node]
    for neighbour in graph[node]:
        if not visited[neighbour] and armySizes[neighbour] < spanningSize:
            spanningSize = dfs(neighbour, graph, visited, armySizes, spanningSize)
    return spanningSize

lines = sys.stdin.readlines()
N = int(lines[0].split()[0])
M = int(lines[0].split()[1])

armySizes = [0] * (N+1)
graph = {}

if M > 0:
    # Build graph from stdin
    for i in range(1, M+1):
        u,v = lines[i].strip().split()
        u = int(u)
        v = int(v)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        
        if v not in graph[u]:
            graph[u].append(v)
        if u not in graph[v]:
            graph[v].append(u)

    # Keep track of each islands army size
    for i in range(1,N+1):
        armySizes[i] = int(lines[M+i].strip())
        
    visited = [False] * (N+1)
    maxArmySize = dfs(1, graph, visited, armySizes, 0)

    print(maxArmySize)
else:
    print(int(lines[1].strip()))