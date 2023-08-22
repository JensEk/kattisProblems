# Problem: https://open.kattis.com/problems/gold
# By: Jens Ekenblad
# Date: 2023-06-14

import sys

lines=sys.stdin.readlines()
w, h = map(int, lines[0].split())



def bdf(pos, graph, gold):
    visited = [False] * (w*h)
    queue = [pos]
    while queue:
        (x,y) = queue.pop(0)
        if not visited[x + (y*len(graph[0]))]:
            visited[x + (y*len(graph[0]))] = True
            print(x, y)
            if graph[y][x] == 'G':
                gold += 1
            if graph[y-1][x] != '#' and graph[y-1][x] != 'T' and not visited[x + ((y-1)*len(graph[0]))]:
                queue.append((x, y-1))
            if graph[y+1][x] != '#' and graph[y+1][x] != 'T' and not visited[x + ((y+1)*len(graph[0]))]:
                queue.append((x, y+1))
            if graph[y][x-1] != '#' and graph[y][x-1] != 'T' and not visited[(x-1) + (y*len(graph[0]))]:
                queue.append((x-1, y))
            if graph[y][x+1] != '#' and graph[y][x+1] != 'T' and not visited[(x+1) + (y*len(graph[0]))]:
                queue.append((x+1, y))
    return gold



gold = 0
goldMap = h*[]
P = True
for line in lines[1:]:
    if P:
        if 'P' in line:
            p = (line.index('P'), len(goldMap))
            P = False
    goldMap.append(line.strip())

amount = bdf(p, goldMap, gold)
print(amount)