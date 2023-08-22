# Problem: https://open.kattis.com/problems/bokforing
# By: Jens Ekenblad
# Date: 2023-07-10

import sys

n, q = map(int, sys.stdin.readline().split())

people = {}
wealth = 0

for i in range(q):
    line = sys.stdin.readline().split()
    if line[0] == "SET":
        people[int(line[1])] = int(line[2])
    elif line[0] == "PRINT":
        print(people.get(int(line[1]), wealth))
    elif line[0] == "RESTART":
        people = {}
        wealth = int(line[1])
