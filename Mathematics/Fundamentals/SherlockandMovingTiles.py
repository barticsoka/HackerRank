l, s1, s2 = (float(x) for x in input().split())

for i in range(int(input())):
    qi = float(input())
    # (qi * 2) ** 0.5       length of the diagonal (desired area)
    # (2 * l ** 2) ** 0.5   length of the diagonal (original squares)
    # (s1 - s2)             speed difference
    print(format(abs(((qi * 2) ** 0.5 - (2 * l ** 2) ** 0.5) / (s1 - s2)), '.20f'))
