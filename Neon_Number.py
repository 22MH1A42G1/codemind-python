a=int(input())
c=pow(a,2)
s=0
while c!=0:
    i=c%10
    s+=i
    c=c//10
su=int(s)
if(a==su):
    print('Neon Number')
else:
    print('Not Neon Number')