n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i%2!=0:
        c+=1
if c<3:
    print("YES")
else:
    print("NO")