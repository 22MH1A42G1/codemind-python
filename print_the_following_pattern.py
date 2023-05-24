n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    if i == 0 or i == n-1:
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*")