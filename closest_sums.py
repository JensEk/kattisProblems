# Problem: https://open.kattis.com/problems/closestsums
# By: Jens Ekenblad
# Date: 2023-07-10

import sys

n = sys.stdin.readline()
cases = 1
while n != "":
    n = int(n)
    numbers = []
    for i in range(n):
        numbers.append(int(sys.stdin.readline()))
    numbers.sort()
    m = int(sys.stdin.readline())
    print(f"Case {cases}:")
    for i in range(m):
        query = int(sys.stdin.readline())
        closestSum = sys.maxsize
        for j in range(len(numbers)):
            for k in range(j + 1, len(numbers)):
                if abs(numbers[j] + numbers[k] - query) < abs(closestSum - query):
                    closestSum = numbers[j] + numbers[k]
        print(f"Closest sum to {query} is {closestSum}.")

    cases += 1
    n = sys.stdin.readline()
