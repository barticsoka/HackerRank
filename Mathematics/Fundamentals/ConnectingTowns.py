# 1
# 33
# 368 341 12 738 901 433 951 833 864 519 552 618 185 248 185 158 439 424 173 781 829 493 224 682 987 370 463 306 943 808 830 967
# expected output 1107662

for i in range(int(input())):
    numberofTowns = int(input())
    routes = [int(x) for x in input().split()]

    choice = 1
    for x in routes:
        choice *= x
    print(choice % 1234567)
