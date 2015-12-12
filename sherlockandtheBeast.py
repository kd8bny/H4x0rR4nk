#!/bin/python3

import sys

def reduce(fives, threes):
    fives = fives[:-1]
    threes += "3" 
    
    return fives, threes
    
def main(n):
    fives = ""
    threes = ""
    for i in range(n):
        fives += "5"
        
    if not len(fives)%3:
        return fives
    else:
        fives, threes = reduce(fives, threes)
    
    while fives != "":
        if not len(threes)%5:
            if not len(fives)%3:
                return fives+threes
        
        fives, threes = reduce(fives, threes)
               
    if not len(threes)%5:
        return threes
    else:
        return -1
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(main(n))
