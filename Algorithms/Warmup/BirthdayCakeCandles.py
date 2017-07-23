#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    
    tallest = max(ar)
    # Generator expression
    return sum(1 for x in ar if x == tallest)
    # List comprehension
    #return len([1 for x in ar if x == tallest])
    # List comprehension v2
    #return len([x for x in ar if x == tallest])
    
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
