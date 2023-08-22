# Problem: https://open.kattis.com/problems/exam
# By: Jens Ekenblad
# Date: 2023-06-06


import sys

k = int(sys.stdin.readline())
myAns = sys.stdin.readline().strip()
friendAns = sys.stdin.readline().strip()

maxAns = len(myAns)
sameAns = 0

for i in range(maxAns):
    if myAns[i] == friendAns[i]:
        sameAns += 1


if sameAns >= k:
    print(k + (maxAns-sameAns))
else:
    print((maxAns-k) + sameAns)

