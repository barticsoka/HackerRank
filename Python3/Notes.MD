# Tips
Use lookup lists

```Python
# Prime factors
prime = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
for i in range(int(input())):
    count, result = 0, 1
    n = int(input())
    for j in prime:
        result *= j
        if(result <= n):
            count += 1
    print(count)

```

# Prime Implementations
[Fastest way to list all primes below n](https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n)
# Operations

```Python
110 & 1     # & is the same as mod(2) or %2
110 % 2

110 >> 1    # Division by two (rounded down to nearest integer)
111 >> 1
```
# Lists

```Python
# list[first element : last element : step size]

list = [1, 2, 3, 4, 5, 6]

# Indexing
list[0]    # first item
list[-1]   # last item

# Slicing
list[0:1]  # first two items
list[-2:]  # last two items (No number after :)
list[::-1] # reverses list order
list[::2]  # every second item

# addition (adding lists together)
[1, 2, 3] + [4, 5, 6] == [1, 2, 3, 4, 5, 6]
# multiplication (repearing list)
[None] * 3 == [None, None, None]
[None, 1] * 3 == [None, 1, None, 1, None, 1]

```