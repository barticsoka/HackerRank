for i in range(int(input())):

    # using map function
    px, py, qx, qy = map(int, input().split())
    print('{0} {1}'.format(2 * qx - px, 2 * qy - py))


for i in range(int(input())):

    # using list comprehension
    px, py, qx, qy = [int(x) for x in input().split()]
    print(2 * qx - px, 2 * qy - py)


for i in range(int(input())):

    # using generator
    px, py, qx, qy = (int(x) for x in input().split())
    print(2 * qx - px, 2 * qy - py)
