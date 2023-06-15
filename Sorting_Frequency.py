from collections import defaultdict
def sort(a,n):
    s=defaultdict(lambda:0)
    for i in range(n):
        s[a[i]]+=1
    a.sort(key=lambda x:(-s[x],x))
    return a
n=int(input())
a=list(map(int,input().split()))
s=sort(a,n)
for i in sorted(set(s),key=s.index):
    print(i,end=' ')