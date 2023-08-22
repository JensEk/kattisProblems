# Problem: https://open.kattis.com/problems/quickbrownfox
# By: Jens Ekenblad
# Date: 2023-06-06


import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
lines = sys.stdin.readlines()[1:]
for line in lines:
    pangram = [False] * 26
    count = 0
    
    line = line.lower().strip()
    for char in line:
        if char.isalpha():
            if pangram[alphabet.index(char)] == False:
                pangram[alphabet.index(char)] = True
                count += 1


    if count == 26:
        print("pangram")
    else:
        missing = ""
        for i in range(len(pangram)):
            if pangram[i] == False:
                missing += alphabet[i]
        print(f'missing {missing}\n')
    