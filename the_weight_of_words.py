# Problem: https://open.kattis.com/problems/weightofwords
# By: Jens Ekenblad
# Date: 2023-06-16

import sys

inp = sys.stdin.readline().strip()
l,w = map(int, inp.split())
alphabet = "_abcdefghijklmnopqrstuvwxyz"

# Create min word of only a's and calculate remaining weight to update each letter
word = ['a']*l
remainingWeight = w - l

# If the weight is larger than max or smaller then whats possible 
if w > 26*int(l) or w < int(l):
    print("impossible")
    quit()

# Print rubish word containing english letters to match weight
for i in range(int(l)):
    if remainingWeight > 26 - alphabet.index(word[i]):
        word[i] = 'z'
        remainingWeight -= 25
    elif remainingWeight > 0:
        word[i] = alphabet[remainingWeight + alphabet.index(word[i])]
        remainingWeight = 0
print("".join(word))

