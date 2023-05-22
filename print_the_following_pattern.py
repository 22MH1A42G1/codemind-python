n=int(input())
for i in range(n):
    for j in range(1,n-2):
        print(j,end="")
    for j in range(n-2,0,-1):
        print(j,end="")
    print()    