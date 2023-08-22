# Problem: https://open.kattis.com/problems/dreamer
# By: Jens Ekenblad
# Date: 2023-08-08

import sys
from datetime import *
from itertools import permutations

t = int(sys.stdin.readline())
bornDate = datetime.strptime("01012000", "%d%m%Y")

# Create all unique permutations of the input then count the valid ones and save the date that is closes to the born date
for _ in range(t):
    date_perm = sorted(
        set(permutations(sys.stdin.readline().strip().replace(" ", ""))),
        key=lambda x: (x[4:], x[2:4], x[:2]),
    )
    possibleDates = 0
    bestDate = None

    for perm in date_perm:
        if len(perm) != 8:
            continue
        day = int(perm[0] + perm[1])
        month = int(perm[2] + perm[3])
        year = int(perm[4] + perm[5] + perm[6] + perm[7])

        if year < 2000:
            continue
        if month > 12 or month < 1:
            continue
        if day > 31 or day < 1:
            continue
        if bestDate == None:
            bestDate = (
                str(perm[0] + perm[1])
                + str(perm[2] + perm[3])
                + str(perm[4] + perm[5] + perm[6] + perm[7])
            )

        try:
            dateValid = datetime(year, month, day)
            possibleDates += 1
        except:
            continue

    if possibleDates > 0:
        print(possibleDates, f"{bestDate[:2]} {bestDate[2:4]} {bestDate[4:]}")
    else:
        print(0)
