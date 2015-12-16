#!/bin/python3

import timeit

def isLow(internList):
    isMod = False
    for value in internList:
        if value == 1:
            isMod = True
        elif value%2 == 0:
            isMod = True
        elif value%5 == 0:
            isMod = True
        else:
            isMod = False
            break
        
    return isMod

def main(internList):
    count = 0
    gMin = min(internList)
    if isLow(internList):
        gMin = 0
    
    for value in internList:
        if value != gMin:
            m = value - gMin
            count += int((m - (m%5))/5)
            count += int((m%5 - ((m%5)%2))/2)
            count += (m%5)%2

    return count
    
#t = int(input())
#for i in range(t):
#    n = int(input())
#    q = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#    print(main(q))

f = open('test3', 'r')
t = int(f.readline())

for i in range(t):
    n = int(f.readline())
    q = [int(arr_temp) for arr_temp in f.readline().strip().split(' ')]
    print(main(q))