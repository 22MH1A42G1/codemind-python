from collections import Counter
n=int(input())
arr1=map(int,input().split())
arr2=dict(Counter(arr1))
arr3=arr2.values()
s=0
for i in arr3:
    s+=i//2
print(s)