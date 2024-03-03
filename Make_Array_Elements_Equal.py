n = int(input())
A = list(map(int, input().split()))
c = 0
for i in range(n):
    cc=0
    for j in range(i,n):
        if A[i] == A[j]:
            cc+=1
            c=max(cc,c)
if len(set(A)) == 1:
    print(0)
else:
    print(c)