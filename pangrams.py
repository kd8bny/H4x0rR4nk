#!/bin/python3

import sys

def main(string):
    pangramCount = ""
    for letter in string.replace(" ", "").lower():
        if not any(letter in letterCount for letterCount in pangramCount):
            pangramCount += letter

    if len(pangramCount) < 26:
        return "not pangram"

    return "pangram"
        
print(main(input()))
