n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in range(n):
    if(a.count(a[i])==1):
        b.append(a[i])
        c+=1
if(c!=0):print(max(b))
else:print('-1')