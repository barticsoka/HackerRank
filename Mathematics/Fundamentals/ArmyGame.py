import sys
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]

n, m = [int(39), int(169)]

# function
def getdrops(x):
    return (x + x % 2) / 2
print(int(getdrops(n) * getdrops(m)))

# lambda expression
getdrops = lambda x : (x + x % 2) / 2
print(int(getdrops(n) * getdrops(m)))

# One liner
print(int((n + n % 2) * (m + m % 2) / 4))

# without division (manipulating bits)
print(((n & 1) + (n >> 1)) * ((m & 1) + (m >> 1)))
