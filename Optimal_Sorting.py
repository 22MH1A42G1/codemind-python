num=int(input())
c=0
for i in range(num):
    a=int(input())
    l=list(map(int,input().split()))
    for j in range(1,a):
        if l[j-1]>l[j]:
            c+=1
    if c==0:
        print(c)
    else:
        ma=max(l)
        mi=min(l)
        print(ma-mi)