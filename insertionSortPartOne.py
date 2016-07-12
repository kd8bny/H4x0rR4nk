#!/bin/python3

import sys

def main(arr):
    e = arr[len(arr)-1]
    for i in range(len(arr)-2, -1, -1):
        if e > arr[i]:
            arr[i+1] = e               
            print(" ".join(str(x) for x in arr))
            break; 
        else:
            arr[i+1] = arr[i]
            print(" ".join(str(x) for x in arr))
            if i == 0:
                arr[i] = e
                print(" ".join(str(x) for x in arr))

    return

size = int( input())
arr = [int(value) for value in input().strip().split(' ')]

main(arr)
