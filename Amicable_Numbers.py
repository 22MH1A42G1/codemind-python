n=int(input())
m=int(input())
p=0
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
for j in range(1,m):
    if(m%j==0):
        p=p+j
if(p==n and s==m):
    print("Amicable")
else:
    print("Not Amicable")