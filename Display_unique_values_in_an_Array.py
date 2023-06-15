n=int(input())
arr=list(map(int,input().split()))
s=set(arr)
c=0
for i in s:
    if i not in arr[arr.index(i)+1:]:
        print(i,end=' ')
        c+=1
if(c==0):
    print(-1)