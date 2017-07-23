#!/bin/python3


def simpleArraySum(n, ar):
    # Complete this function
    tot = 0
    for i in ar:
        tot += i
    return tot

    # or return sum(ar)


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
