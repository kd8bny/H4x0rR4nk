#!/bin/python3

import sys

def main(n, rows):
    a = 0
    b = 0
    for i, row in enumerate(rows):
        a += row[i]
        b += row[(n-1) - i]
    
    return abs(a-b)

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    
print(main(n, a))