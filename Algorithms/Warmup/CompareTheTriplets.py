#!/bin/python3

import sys


def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function

    def score(a, b): return 1 if a > b else 0

    AlicePoints = score(a0, b0) + score(a1, b1) + score(a2, b2)
    BobPoints = score(b0, a0) + score(b1, a1) + score(b2, a2)
    return (AlicePoints, BobPoints)


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))
