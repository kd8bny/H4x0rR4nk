#!/bin/python3

def getLocalMin(internList):
    m = min(internList)
    internSet = set(internList)
    internSet.remove(m)
    m2 = min(internSet)
    for i in range(internList.count(m)-1):
        internList.remove(m)
        
    return m2, internList

def increment(internList, hold):
    countAdj = 0
    m = internList[hold] - min(internList)
    
    incX5 = (m - (m%5))
    if incX5 != 0:
        countAdj = int(incX5/5)
    
    m2 = m%5
    incX2 = (m2 - (m2%2))
    if incX2 != 0:
        countAdj += int(incX2/2)
    
    m1 = m2%2
    incX1 = (m1 - (m1%1))
    if incX1 != 0:
        countAdj += 1
        
    incX = incX5 + incX2 + incX1
    
    for i in range(len(internList)):
        if i != hold:
            internList[i] = internList[i] + incX
            
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
        localMin, internList = getLocalMin(internList)
        hold = internList.index(localMin)
        internList, countAdj = increment(internList, hold)
        isEqual = check(internList)
          
        count += countAdj

    return count
    
t = int(input())
for i in range(t):
    n = int(input())
    q = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    print(main(q))
