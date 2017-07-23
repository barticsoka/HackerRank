for i in range(int(input())):
    n = int(input())
    if n == 1:
        print(n * 2)
    else:
        print(n + 1)

# Using lambda expression (Why?.... Why not! :))
for i in range(int(input())):
    def x(x): return x * 2 if x == 1 else x + 1
    print(x(int(input())))
