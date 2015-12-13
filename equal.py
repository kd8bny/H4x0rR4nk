def getLocalMin(internList):
    internList = set(internList)
    m = min(internList)
    internList.remove(m)
    
    
    if len(internList) < 2:
        doCheck = True
    else:
        doCheck = False
        
    return min(internList), doCheck

def increment(internList, hold):
    countAdj = 0
    m = internList[hold] - min(internList)
    if m >= 5:
        incX = (m - (m%5))
        countAdj = int(incX/5)
    elif m >= 2:
        incX = (m - (m%2))
        countAdj = int(incX/2)
    else:
        incX = 1
        countAdj = 1
    
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
    #print(internList)
    count = 0
    isEqual = False
    while not isEqual:
        #print(internList)
        localMin, doCheck = getLocalMin(internList)
        hold = internList.index(localMin)
        internList, countAdj = increment(internList, hold)
        if doCheck:
            isEqual = check(internList)
          
        count += countAdj
    #print(internList)
    return count
    
t = int(input())
for i in range(t):
    n = int(input())
    q = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    print(main(q))
