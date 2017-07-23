prime = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
for i in range(int(input())):
    count, result = 0, 1
    n = int(input())
    for j in prime:
        result *= j
        if(result <= n):
            count += 1
    print(count)

# Input
n = (614889782588491410,
     614889782588491409,
     614889782588491408,
     614889782588491407,
     6148897825884914,
     614889782588,
     614889782588491410,
     614889782588491411,
     614889782588491412,
     614889782588491413,
     614889782588491415)

# Expected output
test = [15,
        14,
        14,
        14,
        13,
        11,
        15,
        15,
        15,
        15,
        15]

answer = []

for i in n:
    counter, result = 0, 1
    for j in prime:
        result *= j
        if result <= i:
            counter += 1
    answer += [counter]

test == answer
