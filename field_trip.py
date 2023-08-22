# Problem: https://open.kattis.com/problems/fieldtrip
# By: Jens Ekenblad
# Date: 2023-07-10

import sys

lines = sys.stdin.readlines()
n = int(lines[0])
classes = lines[1].split()
lastSect = []

sumClass = sum(list(map(int, classes)))
if sumClass % 3 == 0:
    busCapacity = sumClass / 3
    maxCap = 0
    for k in range(1, n + 1):
        maxCap += int(classes[k - 1])
        if maxCap == busCapacity and len(lastSect) < 2:
            lastSect.append(k)
            maxCap = 0
        elif maxCap > busCapacity:
            print(-1)
            quit()
        elif len(lastSect) == 2:
            break
    print(lastSect[0], lastSect[1])

else:
    print(-1)
