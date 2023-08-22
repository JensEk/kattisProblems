# Problem: https://open.kattis.com/problems/grid
# By: Jens Ekenblad
# Date: 2023-08-07

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(" "))
grid = []

for _ in range(n):
    grid.append([int(x) for x in sys.stdin.readline().strip()])


# Perform BFS from (0, 0) to (n-1, m-1) and count the moves
visited = [[False for _ in range(m)] for _ in range(n)]
queue = deque([(0, 0, 0)])
while queue:
    x, y, d = queue.popleft()
    if x == n - 1 and y == m - 1:
        print(d)
        sys.exit(0)
    for cx, cy in [
        (grid[x][y], 0),
        (-grid[x][y], 0),
        (0, grid[x][y]),
        (0, -grid[x][y]),
    ]:
        newX = x + cx
        newY = y + cy
        if 0 <= newX < n and 0 <= newY < m and not visited[newX][newY]:
            visited[newX][newY] = True
            queue.append((newX, newY, d + 1))

print(-1)
