def half_diamond_star(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print()
n = int(input())
if n >= 3 and n <= 100:half_diamond_star(n)
else:print("The pattern is not possible")