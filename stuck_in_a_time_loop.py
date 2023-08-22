# Problem: https://open.kattis.com/problems/timeloop
# By: Jens Ekenblad
# Date: 2023-06-06


import sys

n = int(sys.stdin.readline())
wizard = "Abracadabra"

for i in range(1,n+1,1):
    print(f'{i} {wizard}')