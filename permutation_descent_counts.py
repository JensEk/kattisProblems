# Problem: https://open.kattis.com/problems/permutationdescent
# By: Jens Ekenblad
# Date: 2023-06-21

import sys

lines = sys.stdin.readlines()
mem = [[0 for i in range(100)] for j in range(101)]

# Calc all descent counts and store in mem to be used for dynamic programming
def pdc(N, v):
    res = 0
    
    if (v == 0 or (v == N-1)):
        return 1
    elif (mem[N][v] != 0):
        return mem[N][v]
    else:
        # Add each possible p(k) times its subproblem in the mem matrix
        res += ((N-v)*pdc(N-1, v-1)) % 1001113
        res += ((v+1)*pdc(N-1, v)) % 1001113 
        mem[N][v] = res % 1001113
        return mem[N][v]

for line in lines[1:]:
    K, N, v = map(int, line.split())
    
    out = pdc(N,v)
    print(f'{K} {out}')