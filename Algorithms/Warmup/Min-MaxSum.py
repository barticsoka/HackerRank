#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
tot = sum(arr)
print("{} {}".format(tot - max(arr), tot - min(arr)))
