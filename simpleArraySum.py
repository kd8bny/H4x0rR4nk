#!/bin/python3

import sys

def main(n, array):
    value = 0
    for i in range(n):
        value += array[i]
        
    return value

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(main(n, arr))
