# Problem: https://open.kattis.com/problems/delimitersoup
# By: Jens Ekenblad
# Date: 2023-08-17

import sys

L = int(sys.stdin.readline())
symbols = sys.stdin.readline().strip()

pushSet = ["(", "[", "{"]
popSet = [")", "]", "}"]
ppSet = {"(": ")", "[": "]", "{": "}", ")": "(", "]": "[", "}": "{"}  # Push-Pop set

stack = []
pos = -1

# Push every opening to stack and then pop and check
for s in symbols:
    pos += 1
    if s in pushSet:
        stack.append(ppSet[s])
    elif s in popSet:
        try:
            test = stack.pop()
        except:
            print(f"{s} {pos}")
            sys.exit(0)
        if s != test:
            print(f"{s} {pos}")
            sys.exit(0)

print("ok so far")
