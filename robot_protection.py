# Problem: https://open.kattis.com/problems/robotprotection
# By: Jens Ekenblad
# Date: 2023-06-25

import sys
import numpy as np

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    if n < 3:
        print('0.0')
    else:
        beaconX = []
        beaconY = []
        beacons = []
        for i in range(n):
            x,y = map(int, sys.stdin.readline().split())
            beacons.append((x,y))
    
        
        # Shoelace formula
        print(0.5*np.abs(np.dot(beaconX,np.roll(beaconY,1))-np.dot(beaconY,np.roll(beaconX,1))))