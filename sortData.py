#!/bin/python3

import sys

def main(rows, k):
    rowsOut = []
    indexArr = []
    for row in rows:
        indexArr.append(row[k])
    indexArr.sort()
    
    for kVal in indexArr:
        for row in rows:
            if row[k] == kVal:
                print(" ".join(str(x) for x in row))
                row[k] = -1
    return

size = [int(value) for value in input().strip().split(' ')] #n x m
rows = [0] * size[0]
for i in range(size[0]):
    rows[i] = [int(value) for value in input().strip().split(' ')]
k = int(input())
    
main(rows, k)
