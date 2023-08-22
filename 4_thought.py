# Problem: https://open.kattis.com/problems/4thought
# By: Jens Ekenblad
# Date: 2023-06-21

import sys

lines = sys.stdin.readlines()[1:]

opSet = ['*', '//', '+', '-']
calcMem = {}

# Pre calculate all possible solutions and store in calcMem to look up into
for x in opSet:
    for y in opSet:
        for z in opSet:
            res = eval(f'4 {x} 4 {y} 4 {z} 4')
            out = f'4 {x} 4 {y} 4 {z} 4 = {res}'
            calcMem[res] = out.replace('//', '/')


for line in lines:
    n = int(line)
    if n in calcMem:
        print(calcMem[n])
    else:
        print('no solution')