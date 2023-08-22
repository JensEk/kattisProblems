# Problem: https://open.kattis.com/problems/annoyedcoworkers
# By: Jens Ekenblad
# Date: 2023-08-07

import sys
import heapq

h, c = map(int, sys.stdin.readline().split())
coworkers = []

# Add all coworkers by initial annoyance level + 1d to have base case to sort from
for _ in range(c):
    a, d = map(int, sys.stdin.readline().split())
    coworkers.append((a + d, d))

# Use minheap to always increment the worker with smallest annoyance level, then print the largest
heapq.heapify(coworkers)
for _ in range(h):
    a, d = heapq.heappop(coworkers)
    heapq.heappush(coworkers, (a + d, d))

max = -1
for a, d in coworkers:
    m = a - d
    if m > max:
        max = m
print(max)
