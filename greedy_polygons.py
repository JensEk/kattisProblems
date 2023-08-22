# Problem: https://open.kattis.com/problems/greedypolygons
# By: Jens Ekenblad
# Date: 2023-06-28

import sys
from math import tan, pi

lines = sys.stdin.readlines()

for line in lines[1:]:
    n,l,d,g = map(int, line.split())
    regPoly = l * l * n / (tan(pi / n) * 4)
    extPoly = n * d * g * l
    cirlArea = pi * d * g * d * g
    print(regPoly + extPoly + cirlArea)