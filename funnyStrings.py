#!/bin/python3

import sys

def main(string):
    index = tuple('abcdefghijklmnopqrstuvwxyz')

    for i in range(1, len(string)):
        S = abs(index.index(string[i]) - index.index(string[i-1]))
        R = abs(index.index(string[len(string)-i]) - index.index(string[len(string)-i-1]))
        
        if S != R:
            return "Not Funny"
        
    return "Funny"
    
for i in range(int(input())): 
    print(main(input()))
