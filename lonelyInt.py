#!/usr/bin/py

def main(intList):
    answer = 0
    for value in intList:
        if intList.count(value) == 1:
            answer = value
            break
            
    return answer

if __name__ == '__main__':
    a = int(input())
    b = [int(val) for val in input().strip().split(" ")]
    print(main(b))
    