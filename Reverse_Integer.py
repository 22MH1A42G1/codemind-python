x = (input())
s=""
for i in x:
    if i!='-' and i!='0':
        s+=i
    elif i=='-':
        print("-",end="")
print(s[::-1])