# Problem: https://open.kattis.com/problems/cudoviste
# By: Jens Ekenblad
# Date: 2023-08-09

import sys

r, c = map(int, sys.stdin.readline().split(" "))
park = []
output = [0] * 5

for _ in range(r):
    line = sys.stdin.readline().strip()
    park.append([symbol for symbol in line])

# Check where surrounding buildings are and then look for cars to squash to find the number of parking spaces
for i in range(1, r):
    for j in range(1, c):
        if (
            park[i][j] != "#"
            and park[i - 1][j] != "#"
            and park[i][j - 1] != "#"
            and park[i - 1][j - 1] != "#"
        ):
            spaces = 0
            if park[i][j] == "X":
                spaces += 1
            if park[i - 1][j] == "X":
                spaces += 1
            if park[i][j - 1] == "X":
                spaces += 1
            if park[i - 1][j - 1] == "X":
                spaces += 1
            output[spaces] += 1

for res in output:
    print(res)
