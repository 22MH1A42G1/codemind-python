n=int(input())
a=10
sq=0
i=0
while True:
    if n<a:
        sq=n**2
        d=sq%a
        if n==d:
            print("Automorphic Number")
            break
        else:
            print("Not an Automorphic Number")
            break
    a=a*10
    i+=1