#!/bin/python3

def decrement(internList):
    countAdj = 0
    gMax = max(internList)
    gMin = min(internList)
    m = gMax - gMin
    
    incX5 = (m - (m%5))
    if incX5 != 0:
        countAdj = int(incX5/5)
    
    m2 = m%5
    incX2 = (m2 - (m2%2))
    if incX2 != 0:
        countAdj += int(incX2/2)
    
    incX1 = m2%2
    countAdj += m2%2
        
    incX = incX5 + incX2 + incX1

    internList[internList.index(gMax)] -= incX
            
    return internList, countAdj

def check(internList):
    if internList.count(internList[0]) == len(internList):
        return True
    else:
        return False

def main(internList):
    count = 0
    isEqual = False
    while not isEqual:
        internList, countAdj = decrement(internList)
        isEqual = check(internList)
          
        count += countAdj

    return count
    
t = int(input())
for i in range(t):
    n = int(input())
    q = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    print(main(q))
