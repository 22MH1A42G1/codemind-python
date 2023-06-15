n=int(input())
a=list(map(int,input().split()))
s=0
s1=0
for i in range(n):
    if(i%2==0):
        s=s+a[i]
    else:
        s1=s1+a[i]
b=abs(s-s1)
if(b%4==0):
    print('X')
else:
    print('Y')