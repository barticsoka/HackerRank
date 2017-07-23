#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int, raw_input().strip().split(' '))
    a.append(a_temp)

total = 0
for i in range(n):
    row = a[i]
    total += int(row[i]) - int(row[-(i + 1)])
print(abs(total))
