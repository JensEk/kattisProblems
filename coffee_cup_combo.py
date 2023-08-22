# Problem: https://open.kattis.com/problems/coffeecupcombo
# By: Jens Ekenblad
# Date: 2023-06-06


import sys

n = int(sys.stdin.readline())
machines = sys.stdin.readline().strip()
maxLect = 0
coffes = 0

for i in range(n):
    if machines[i] == "1":
        coffes = 2
        maxLect += 1
    else:
        if coffes > 0:
            coffes -= 1
            maxLect += 1    

print(maxLect)   
