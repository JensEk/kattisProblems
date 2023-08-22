# Problem: https://open.kattis.com/problems/sjecista
# By: Jens Ekenblad
# Date: 2023-07-10

import sys

n = int(sys.stdin.readline())

if n < 4:
    print(0)
else:
    print(n * (n - 3) * (n - 2) * (n - 1) // 24)
