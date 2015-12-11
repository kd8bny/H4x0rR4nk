#!/bin/python3

import sys

def main(n):
    if n == 0:
        return 1
    
    elif n == 1:
        return n*2
    
    else:
        h = 1
        for i in range(1, n+1):
            if i%2:
                h = h * 2
            else:
                h = h + 1
        return h

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(main(n))
