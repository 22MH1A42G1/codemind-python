num=list(str(int(input())))
for i in range(len(num)):
    if num[i]=="6":
        num[i]="9"
        break
num = "".join(num)
print(num)