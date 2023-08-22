# Problem: https://open.kattis.com/problems/goatrope
# By: Jens Ekenblad
# Date: 2023-06-24

import sys

line = sys.stdin.readline()
x,y,x1,y1,x2,y2 = map(int, line.split())
dx, dy = 0, 0

# Find min distance dx,dy to the rectangle
if x < x1:
    dx = x1 - x
elif x > x2:
    dx = x - x2
if y < y1:
    dy = y1 - y
elif y > y2:
    dy = y - y2

# pythogoras to find distance
print((dx**2 + dy**2)**0.5)