n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if((i==j) or ((i+j)==(n-1))):
            print("x",end="")
        else:
            print("0",end="")
    print()        