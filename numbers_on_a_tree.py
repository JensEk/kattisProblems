# Problem: https://open.kattis.com/problems/numbertree
# By: Jens Ekenblad
# Date: 2023-06-14

import sys

inp=sys.stdin.readline().split()
H = int(inp[0])

if not len(inp) == 1:
    path = inp[1]

    index = 1
    for p in (path):
        if p == "L":
            index = 2*(index)
        else:
            index = 2*(index) + 1

    print(2**(H+1) - index)
else:
    print(2**(H+1) - 1)
