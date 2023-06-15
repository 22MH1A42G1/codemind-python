n=int(input())
se=0
so=0
a=list(map(int,input().split()))
for i in range(n):
    if(i%2==0):
        se=se+a[i]
    else:
        so=so+a[i]
if(se-so==0):
    print('YES')
else:
    print('NO')