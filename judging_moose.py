# Problem: https://open.kattis.com/problems/judgingmoose
# By: Jens Ekenblad
# Date: 2023-06-06


import sys

line = sys.stdin.readline().split(" ")
l = int(line[0])
r = int(line[1])

if l == 0 and r == 0:
    print('Not a moose')
elif l == r:
    print(f'Even {l+r}')
else:
    maxPoints = max(l, r)
    maxPoints *= 2
    print(f'Odd {maxPoints}')
