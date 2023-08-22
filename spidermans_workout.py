# Problem: https://open.kattis.com/problems/spiderman
# By: Jens Ekenblad
# Date: 2023-08-10

import sys

N = int(sys.stdin.readline())

for _ in range(N):
    M = int(sys.stdin.readline())
    distances = list(map(int, sys.stdin.readline().split(" ")))

    # Use dynamic programming to find min/max height to climb at each i:th distance
    dp = [[-1 for j in range(1001)] for i in range(41)]
    dp[0][0] = 0
    direction = [[0 for j in range(1001)] for i in range(41)]
    result = [0] * (M + 1)
    position = 0

    for i in range(1, M + 1):
        for j in range(1000 - distances[i - 1] + 1):
            up = j + distances[i - 1]
            down = j - distances[i - 1]
            if down >= 0:
                if dp[i - 1][up] != -1:
                    dp[i][j] = dp[i - 1][up]
                    direction[i][j] = -1
                if dp[i - 1][down] != -1:
                    if dp[i][j] == -1 or dp[i][j] > max(j, dp[i - 1][down]):
                        dp[i][j] = max(j, dp[i - 1][down])
                        direction[i][j] = 1
            elif dp[i - 1][up] != -1:
                dp[i][j] = dp[i - 1][up]
                direction[i][j] = -1
    for i in range(M, 0, -1):
        result[i] = direction[i][position]
        position -= direction[i][position] * distances[i - 1]
    if dp[M][0] > -1:
        print("".join(["U" if result[i] == 1 else "D" for i in range(1, M + 1)]))
    else:
        print("IMPOSSIBLE")
