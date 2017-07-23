#!/bin/python3

import sys

n = int(input().strip())

size = n

while n > 0:
    print(('#' * (size - n + 1)).rjust(size, ' '))
    n -= 1
