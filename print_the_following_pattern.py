n=int(input())
for i in range(n):
    for j in range(n):
        if not(i==j):print('x',end="")
        else:print('0',end="")
    print()    