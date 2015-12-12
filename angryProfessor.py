#!/bin/python3

import sys

def main(k, array):
    count = 0
    for i in array:
        if i <= 0:
            count += 1
    
    if count >= k: 
        return "NO"
    else:
        return "YES"    

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    
    print(main(k, a))
