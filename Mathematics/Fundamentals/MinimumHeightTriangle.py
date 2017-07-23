import sys


def lowestTriangle(base, area):
    # Complete this function
    x = area * 2 / base
    if x % 1 != 0:
        return int(x + 1)
    else:
        return int(x)


base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
